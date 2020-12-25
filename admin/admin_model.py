from app import admin, db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from utils.model_utils import UtilityMixin, PlansView
from sqlalchemy import func


class Plans(UtilityMixin, db.Model):
    """ Plans model for storing various insurance plans """

    id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=lambda: uuid4().hex,
        primary_key=True,
    )
    plan_name = db.Column(db.String(100), unique=True, index=True, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    payment_frequency = db.Column(db.String(20), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, **kwargs):
        for field in list(kwargs.keys()):
            setattr(self, field, kwargs[field])

    def __repr__(self):
        return f"<Plans >>> {self.plan_name}>"


admin.add_view(PlansView(Plans, db.session))
