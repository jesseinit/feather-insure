import json


class TestUserResourceEndpoints:
    def test_user_login_successfull(self, client, new_user):
        """ Test for a successful user login """
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
        assert response.status_code == 200
        assert resp["message"] == "Login was successfull"
        assert "token" in resp["data"].keys()

    def test_user_login_unsuccessfull_wrong_password(self, client, new_user):
        """ Test for an unsuccessful user login with a bad password """
        response = client.post(
            "/api/v1/user/login",
            data=json.dumps(
                {
                    "email": new_user.email,
                    "password": "someWrongPassword",
                }
            ),
        )

        resp = response.get_json()
        assert response.status_code == 401
        assert resp["message"] == "Your email or password is not correct"
        assert resp["status"] == "failed"

    def test_user_login_unsuccessfull(self, client):
        """ Test for an unsuccessful user login for a non-existing user """
        response = client.post(
            "/api/v1/user/login",
            data=json.dumps(
                {
                    "email": "non.existing@mail.com",
                    "password": "IdontKnowHowHeDidIt",
                }
            ),
        )

        resp = response.get_json()
        assert response.status_code == 401
        assert resp["message"] == "Your email or password is not correct"
        assert resp["status"] == "failed"
