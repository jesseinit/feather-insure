from utils.base_schema import BaseSchema
from marshmallow import fields, validate


class RegisterSchema(BaseSchema):
    first_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=50, error="First name should contain 2 to 50 characters"
        ),
        error_messages={"required": "You've not entered your First Name"},
    )
    last_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=50, error="Last name should contain 2 to 50 characters"
        ),
        error_messages={"required": "You've not entered your Last Name"},
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": "You've not entered your Email Address",
            "invalid": "Please enter a valid email address",
        },
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(
            min=6, max=50, error="Password should contain 6 to 50 characters"
        ),
        error_messages={"required": "You've not entered your password"},
    )
