import pytest
from user.user_model import User


@pytest.fixture()
def new_user():
    new_user = User(
        first_name="Dummy",
        last_name="Jones",
        email="john.doe@feather-insurance.com",
        password="show-me-the-way",
    ).save()
    return new_user
