import json


class TestUserResourceEndpoints:
    def test_user_signup_successfull(self, client):
        """ Test for a successful user signup """
        response = client.post(
            "/api/v1/user/register",
            data=json.dumps(
                {
                    "email": "john.doe@feather-insurance.com",
                    "password": "inflames",
                    "first_name": "Jesse",
                    "last_name": "Extraordinaire",
                }
            ),
        )

        resp = response.get_json()
        assert response.status_code == 201
        assert resp["message"] == "Your account has been created successfully"
        assert resp["data"]["email"] == "john.doe@feather-insurance.com"
        assert resp["data"]["first_name"] == "Jesse"
        assert resp["data"]["last_name"] == "Extraordinaire"

    def test_unsuccessfull_user_signup(self, client, new_user):
        """ Test for a unsuccessful user signup """
        response = client.post(
            "/api/v1/user/register",
            data=json.dumps(
                {
                    "email": "john.doe@feather-insurance.com",
                    "password": "inflames",
                    "first_name": "Jesse",
                    "last_name": "Extraordinaire",
                }
            ),
        )

        resp = response.get_json()
        assert response.status_code == 409
        assert resp["message"] == "This email address has been taken"
        assert resp["status"] == "conflict"
