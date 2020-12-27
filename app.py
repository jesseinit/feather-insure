from flask import Flask, jsonify
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv

load_dotenv()
from config import config
from utils.validations import ValidationError


DB_NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)
db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
flask_bcrypt = Bcrypt()
jwt = JWTManager()
redis_client = FlaskRedis()
admin = Admin()


def create_app(config_name):
    """ Creates an application factory """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)
    admin.init_app(app)
    redis_client.init_app(app)
    from admin.admin_blueprint import admin_blueprint
    from questionnaire.questionnaire_blueprint import questionnaire_blueprint
    from user.user_blueprint import user_blueprint

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(questionnaire_blueprint)

    @app.errorhandler(ValidationError)
    def handle_exception(error):
        """Error handler called when a ValidationError Exception is raised"""

        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(500)
    def internal_server_error(error):
        return {"message": "Internal Server Error", "status": "error"}, 500

    @jwt.invalid_token_loader
    def invalid_token_loader(expired_token):
        return {
            "status": "error",
            "message": "Your session is invalid. Kindly login again",
        }, 401

    @jwt.unauthorized_loader
    def no_auth_header_handler(error):
        return {
            "status": "error",
            "message": "Authentication type should be a bearer type.",
        }, 401

    @jwt.expired_token_loader
    def my_expired_token_handler(error):
        return {
            "status": "error",
            "message": "Your session has expired. Kindly login again.",
        }, 401

    return app
