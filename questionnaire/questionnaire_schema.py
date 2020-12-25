from utils.base_schema import BaseSchema
from marshmallow import fields, validate, INCLUDE

from utils.validations import ValidationError


class QuestionnaireSchema(BaseSchema):
    class Meta:
        unknown = INCLUDE

    first_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=50, error="First name should contain 2 to 50 characters"
        ),
        error_messages={"required": "You've not entered your First Name"},
    )
    address = fields.Str(
        required=True,
        validate=validate.Length(
            min=5, max=200, error="Address should contain 5 to 200 characters"
        ),
        error_messages={"required": "You've not entered an address"},
    )
    has_children = fields.Boolean(required=True)
    occupation = fields.Str(
        required=True, validate=validate.OneOf(["Employed", "Student", "Self-employed"])
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": "You've not entered your Email Address",
            "invalid": "Please enter a valid email address",
        },
    )
    children_count = fields.Method("compute_children_count")

    def compute_children_count(self, obj):
        if "has_children" in obj.keys() and obj["has_children"] is True:
            if "children_count" not in obj.keys() or obj["children_count"] < 1:
                raise ValidationError(
                    {
                        "message": {
                            "children_count": [
                                "Enter a the number of children you have"
                            ]
                        }
                    },
                    status_code=422,
                )
        return obj.get("children_count")
