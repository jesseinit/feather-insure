from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/api/v1/user")


@user_blueprint.route("/register", methods=["POST"])
def register_user():
    """ This route handles all user creation and registration  """
    return {"id": "some-user-id"}
