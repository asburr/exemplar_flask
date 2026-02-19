
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
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    db.init_app(app)
    app.register_blueprint(testbp.bp)
    return app
