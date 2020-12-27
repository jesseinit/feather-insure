from uuid import uuid4

from app import admin, db

from app import flask_bcrypt as BCrypt
from sqlalchemy import event, func
from sqlalchemy.dialects.postgresql import UUID
from utils.model_utils import UtilityMixin, UserView


class User(UtilityMixin, db.Model):  # type: ignore
    """ User model for storing user related information """

    id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=lambda: uuid4().hex,
        primary_key=True,
    )
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, **kwargs):
        for field in list(kwargs.keys()):
            setattr(self, field, kwargs[field])

    def __repr__(self):
        return f"<User >>> {self.email}>"


@event.listens_for(User, "before_insert")
def hash_user_password(mapper, connection, self):
    self.password = BCrypt.generate_password_hash(self.password).decode("utf-8")


admin.add_view(UserView(User, db.session))
