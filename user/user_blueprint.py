from flask import Blueprint
from flask import request
from utils.validations import validate_json_request, validate_schema
from user.user_schema import RegisterSchema

from user.user_model import User as UserModel

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/api/v1/user")


@user_blueprint.route("/register", methods=["POST"])
@validate_json_request(request)
@validate_schema(request, RegisterSchema())
def register_user():
    """ This route handles all user creation and registration  """
    user_info = request.get_json()
    existing_user = UserModel.query.filter_by(email=user_info["email"]).first()
    if existing_user:
        return {
            "message": "This email address has been taken",
            "status": "conflict",
        }, 409
    new_user = UserModel(**user_info).save()
    return {
        "message": "Your account has been created successfully",
        "status": "success",
        "data": RegisterSchema(exclude=["password"]).dump(new_user),
    }, 201


@user_blueprint.route("/login", methods=["POST"])
def login_user():
    """ This route handles user login  """
    return {"token": "some-generated-toke", "profile_data": {}}
