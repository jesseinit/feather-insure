import os
from config import config

from user.user_blueprint import user_blueprint

from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name):
    """ Creates an application factory """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user_blueprint)

    return app
