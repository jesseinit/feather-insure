import json


class TestQuestionnaireResourceEndpoints:
    def test_valid_questionnaire_submision(
        self, client, logged_in_user_token, setup_plans
    ):
        """ Test for questionnaira submission with valid data """
        response = client.post(
            "/api/v1/questionnaire/process",
            data=json.dumps(
                {
                    "first_name": "Jesse",
                    "address": "No 8, Heaven Gates Drive, Santorini, Greece",
                    "occupation": "Employed",
                    "has_children": False,
                    "email": "bigmanjesse@gmail.com",
                    "children_count": 2,
                }
            ),
            headers={"authorization": f"Bearer {logged_in_user_token}"},
        )

        resp = response.get_json()
        assert response.status_code == 200
        assert resp["message"] == "Here is your recommendation"
        assert "highly_recommended" in resp["data"].keys()
        assert "least_recommended" in resp["data"].keys()
        assert "recommended" in resp["data"].keys()
