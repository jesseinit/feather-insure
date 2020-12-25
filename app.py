from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from mockredis import MockRedis
from sqlalchemy import MetaData


from config import config
from utils.validations import ValidationError

load_dotenv()

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
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
    # if app.testing:
    #     redis_client = FlaskRedis.from_custom_provider(MockRedis)
    # else:
    #     redis_client = FlaskRedis()
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

    return app
