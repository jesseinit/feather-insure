from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from app import flask_bcrypt as BCrypt
from utils.validations import validate_json_request, validate_schema
from user.user_schema import RegisterSchema, LoginSchema, UserProfileSchema

from user.user_model import User as UserModel

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/api/v1/user")


@user_blueprint.route("/register", methods=["POST"])
@validate_json_request(request)
@validate_schema(request, RegisterSchema())
def register_user():
    """ This route handles all user creation and registration  """
    user_info = request.get_json()
    existing_user_instance = UserModel.query.filter_by(email=user_info["email"]).first()
    if existing_user_instance:
        return {
            "message": "This email address has been taken",
            "status": "conflict",
        }, 409
    new_user_instance = UserModel(**user_info).save()
    return {
        "message": "Your account has been created successfully",
        "status": "success",
        "data": RegisterSchema(exclude=["password"]).dump(new_user_instance),
    }, 201


@user_blueprint.route("/login", methods=["POST"])
@validate_json_request(request)
@validate_schema(request, LoginSchema())
def login_user():
    """ This route handles user login  """
    user_info = request.get_json()
    user_instance = UserModel.query.filter_by(email=user_info["email"]).first()
    if not user_instance:
        return {
            "message": "Your email or password is not correct",
            "status": "failed",
        }, 401
    is_valid_password = BCrypt.check_password_hash(
        user_instance.password, user_info["password"]
    )
    if not is_valid_password:
        return {
            "message": "Your email or password is not correct",
            "status": "failed",
        }, 401
    token = create_access_token(identity={"id": user_instance.id})
    return {
        "message": "Login was successfull",
        "status": "success",
        "data": dict(
            token=token,
            profile=UserProfileSchema(exclude=["password"]).dump(user_instance),
        ),
    }, 200
