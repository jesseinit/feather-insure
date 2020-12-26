from functools import wraps


class ValidationError(Exception):
    """Base Validation class for handling validation errors"""

    def __init__(self, error, status_code=None):
        super().__init__(self)
        self.status_code = 400
        self.error = error
        self.error["status"] = "error"
        self.error["message"] = error["message"]

        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return self.error


def validate_json_request(request):
    """Decorator function to check for json content type in request"""

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if (
                not request.data.decode("utf-8")
                or not request.get_json(force=True).keys()
            ):
                raise ValidationError(
                    {"status": "error", "message": "Empty JSON Request"}, 400
                )
            return func(*args, **kwargs)

        return decorated_function

    return decorator


def validate_schema(request, schema_instance):
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            json_payload = request.get_json()
            schema_instance.load_json_into_schema(json_payload)
            return func(*args, **kwargs)

        return wrapper_function

    return decorator
