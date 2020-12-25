import pytest
from user.user_model import User
import json


@pytest.fixture()
def new_user():
    new_user = User(
        first_name="Dummy",
        last_name="Jones",
        email="john.doe@feather-insurance.com",
        password="show-me-the-way",
    ).save()
    return new_user


@pytest.fixture()
def logged_in_user_token(client, new_user):
    print("HERE CALLLLLLED")
    response = client.post(
        "/api/v1/user/login",
        data=json.dumps(
            {
                "email": new_user.email,
                "password": "show-me-the-way",
            }
        ),
    )
    resp = response.get_json()
    print(resp["data"])
    return resp["data"]["token"]
