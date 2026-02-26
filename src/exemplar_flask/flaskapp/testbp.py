""" This module is a flask project to demo REST endpoints and REST clients. """
try:
  from flask_smorest import Blueprint
  from marshmallow import (Schema, fields)
except ImportError:
  from flask import Blueprint
from flask import (request, jsonify)
from .db import get_db
from functools import wraps

mapping = {str: fields.Str(required=True), int: fields.Int(), 
           bool: fields.Bool(), float: fields.Float()}

def http_response(code:int=200,columns:dict[str,type]=None):
  """ Success response code if using smorest. """
  if columns is None: columns={}
  def decorator(f):
    if hasattr(bp, 'response'):
        marshmallow_columns = {k: mapping[v] for k, v in columns.items()}
        schema = Schema.from_dict(marshmallow_columns,name=f"{f.__name__}_response")
        return bp.response(code, schema)(f)
    return f
  return decorator

def http_arguments(params: dict[str, type]):
  """ Extracts arguments from the http query parameters. """
  def decorator(f):
    if hasattr(bp, 'arguments'):
        marshmallow_params = {k: mapping[v] for k, v in params.items()}
        schema = Schema.from_dict(marshmallow_params,name=f"{f.__name__}_request_args")
        return bp.arguments(schema, location="query", as_kwargs=True)(f)
    else:
      """ Decorator runs once and creates the wrapper. """
      @wraps(f)
      def wrapper(*args, **kwargs):
        """ Wrapper runs every API call and passes args as keyword param to API. """
        for k in params.keys():
          kwargs[k] = request.args.get(k)
        return f(*args, **kwargs)
      return wrapper
  return decorator

def http_jsonbody(params: dict[str, type]):
  """ Extracts arguments from the http json body. """
  def decorator(f):
    if hasattr(bp, 'arguments'):
        mapping = {str: fields.Str(required=True), int: fields.Int(), 
                   bool: fields.Bool(), float: fields.Float()}
        marshmallow_params = {k: mapping[v] for k, v in params.items()}
        schema = Schema.from_dict(marshmallow_params,name=f"{f.__name__}_request_json")
        return bp.arguments(schema, location="json", as_kwargs=True)(f)
    else:
      """ Decorator runs once and creates the wrapper. """
      @wraps(f)
      def wrapper(*args, **kwargs):
        """ Wrapper runs every API call and passes args as keyword param to API. """
        j = request.get_json() or {}
        for k in params.keys():
          kwargs[k] = j.get(k)
        return f(*args, **kwargs)
      return wrapper
  return decorator

bp = Blueprint('db', __name__, url_prefix='/db')

@bp.errorhandler(422)
def handle_unprocessable_entity(err):
  """ Output more information to help debug 422 error codes. """
  data = getattr(err, "messages", "No message")
  print(f"Validation Error: {data}")
  return {"error": "Unprocessable Entity", "details": data}, 422

@bp.after_request
def log_request_response(response):
    print("\n--- REQUEST ---")
    print(f"URL: {request.method} {request.url}")
    print(f"Headers: {dict(request.headers)}")
    if request.is_json:
        print(f"Body: {request.get_json()}")
    print("--- RESPONSE ---")
    print(f"Status: {response.status}")
    if response.is_json:
        print(f"Body: {response.get_json()}")
    print("----------------\n")
    return response
  
test_columns={"id":int,"field1":str,"field2":str}
test2_columns={"id":int,"test_id":str,"created": str, "field2":str,"field3":str}

@bp.route('/test/<field1>', methods=['POST'])
@http_response(200)
@http_jsonbody({"field2":str})
def test_post(field1,field2):
  """ Add row into test. """
  db = get_db()
  try:
    db.execute("INSERT INTO test (field1, field2) VALUES (?, ?)",(field1, field2))
    db.commit()
  except db.IntegrityError:
    return f"field1={field1} and must be unique.", 400
  return f"{field1} added", 200

@bp.route('/test/<field1>', methods=['GET'])
@http_response(200,test_columns)
def test_get(field1):
  """ Get row from test. """
  db = get_db()
  cursor = db.cursor()
  cursor.execute("SELECT * FROM test WHERE field1 = ?",(field1,))
  row = cursor.fetchone()
  if row is None:
    return f"field1={field1} does not exist.", 400
  return jsonify({x[0]: x[1] for x in zip(test_columns,row)}), 200

@bp.route('/test/<testid>/test2/<field2>', methods=['POST'])
@http_response(200)
@http_jsonbody({"field3":str})
def test2_post(testid,field2,field3):
  """ Add row to test2 with foreign key to test. """
  db = get_db()
  try:
    db.execute("INSERT INTO test2 (test_id, field2, field3) VALUES (?, ?, ?)",(testid, field2,field3))
    db.commit()
  except db.IntegrityError:
    return f"field2={field2} and must be unique.", 400
  return f"{field2} added", 200

@bp.route('/test/<testid>/test2/<field2>', methods=['GET'])
@http_response(200,test2_columns)
def test2_get(testid,field2):
  """ Get row from test2. """
  db = get_db()
  cursor = db.cursor()
  cursor.execute("SELECT * FROM test2 WHERE field2 = ?",(field2,))
  row = cursor.fetchone()
  if row is None:
    return f"field2={field2} does not exist.", 400
  return jsonify({x[0]: x[1] for x in zip(test2_columns,row)}), 200
