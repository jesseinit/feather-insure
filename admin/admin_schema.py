from app import ma
from admin.admin_model import Plans


class PlansModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plans
