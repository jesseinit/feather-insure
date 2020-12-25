from flask import Blueprint
from admin.admin_model import Plans

admin_blueprint = Blueprint("admin_blueprint", __name__, url_prefix="/api/v1/admin")

# This file is just to allow the admin extension detect the imported model
