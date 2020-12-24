from marshmallow import exceptions, Schema


class BaseSchema(Schema):
    def load_json_into_schema(self, data):
        """Helper function to load raw json(deserialized data) request data
        into schema"""
        try:
            data = self.loads(data)
        except exceptions.ValidationError as e:
            from utils.validations import ValidationError

            raise ValidationError(dict(message=e.messages), 422)
        return data
