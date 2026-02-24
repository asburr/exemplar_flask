
import os
from flask import Flask
from . import db
from . import testbp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev',DATABASE='test/flask.sqlite')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)
    try:
      from flask_smorest import Api
      app.config["API_TITLE"] = "Test API"
      app.config["API_VERSION"] = "v1"
      app.config["OPENAPI_VERSION"] = "3.0.3"
      app.config["OPENAPI_URL_PREFIX"] = "/"
      app.config["OPENAPI_JSON_PATH"] = "openapi.json"
      app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
      app.config["OPENAPI_SWAGGER_UI_URL"] = "/static/swagger-ui/"
      app.config["API_SPEC_OPTIONS"] = {
        "components": {
          "schemas": {
              "Error": {
                  "type": "object",
                  "properties": {
                      "code": {"type": "integer"},
                      "message": {"type": "string"},
                      "errors": {"type": "object"}
                  }
              }
          },
          "responses": {
              "UNPROCESSABLE_ENTITY": {
                  "description": "Unprocessable Entity",
                  "content": {
                      "application/json": {
                          "schema": {"$ref": "#/components/schemas/Error"}
                      }
                  }
              }
          }
        }
      }
      api = Api(app)
      api.register_blueprint(testbp.bp)
    except:
      app.register_blueprint(testbp.bp)
    return app
