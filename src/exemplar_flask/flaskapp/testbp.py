try:
  from flask_smorest import Blueprint
  from marshmallow import Schema
except ImportError:
  from flask import Blueprint
from flask import (request, jsonify)
from .db import get_db

def smorest_response(params:dict[str,type], code:int=200):
  if hasattr(bp, 'response'):
      return bp.response(code)
  return lambda f: f  # Do nothing if standard Flask

def smorest_arguments(params:dict[str,type], code:int=200):
  if hasattr(bp, 'arguments'):
    schema = Schema.from_dict(params)
    return bp.arguments(schema, location="query")
  return lambda f: f  # Do nothing if standard Flask

bp = Blueprint('db', __name__, url_prefix='/db')
test_titles=["id","field1","field2"]
test2_titles=["id","test_id","field2","field3"]

@bp.route('/test/<field1>', methods=['POST'])
@smorest_response(200)
@smorest_arguments({"field2":str})
def test_post(query_args,field1):
  if query_args:
    field2 = query_args.get('field2')
  else:
    field2 = request.args.get('field2')
  db = get_db()
  try:
    db.execute("INSERT INTO test (field1, field2) VALUES (?, ?)",(field1, field2))
    db.commit()
  except db.IntegrityError:
    return f"field1={field1} and must be unique.", 400
  return f"{field1} added", 200

@bp.route('/test/<field1>', methods=['GET'])
@smorest_response(200)
def test_get(field1):
  db = get_db()
  cursor = db.cursor()
  cursor.execute("SELECT * FROM test WHERE field1 = ?",(field1,))
  row = cursor.fetchone()
  if row is None:
    return f"field1={field1} does not exist.", 400
  return jsonify({x[0]: x[1] for x in zip(test_titles,row)}), 200

@bp.route('/test/<testid>/test2/<field2>', methods=['POST'])
@smorest_response(200)
@smorest_arguments({"field3":str})
def test2_post(query_args,testid,field2):
  if query_args:
    field3 = query_args.get('field3')
  else:
    field3 = request.args.get('field3')
  db = get_db()
  try:
    db.execute("INSERT INTO test2 (test_id, field2, field3) VALUES (?, ?, ?)",(testid, field2,field3))
    db.commit()
  except db.IntegrityError:
    return f"field2={field2} and must be unique.", 400
  return f"{field2} added", 200

@bp.route('/test/<testid>/test2/<field2>', methods=['GET'])
@smorest_response(200)
def test2_get(testid,field2):
  db = get_db()
  cursor = db.cursor()
  cursor.execute("SELECT * FROM test2 WHERE field2 = ?",(field2,))
  row = cursor.fetchone()
  if row is None:
    return f"field2={field2} does not exist.", 400
  return jsonify({x[0]: x[1] for x in zip(test2_titles,row)}), 200

