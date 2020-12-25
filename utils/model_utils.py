from app import db
from flask_admin.contrib.sqla import ModelView


class UtilityMixin:
    def save(self):
        """Function for saving new objects"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """Function for updating objects"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self.save()


class UserView(ModelView):
    column_display_pk = True
    column_exclude_list = [
        "password",
    ]

class PlansView(ModelView):
    column_display_pk = True
