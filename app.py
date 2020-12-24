import os
from config import config


from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
ma = Marshmallow()
flask_bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name):
    """ Creates an application factory """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)
    from user.user_blueprint import user_blueprint

    app.register_blueprint(user_blueprint)
    from utils.validations import ValidationError

    @app.errorhandler(ValidationError)
    def handle_exception(error):
        """Error handler called when a ValidationError Exception is raised"""

        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app
