import json
from flask import Blueprint, request
from app import redis_client
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.validations import validate_json_request, validate_schema
from admin.admin_model import Plans
from questionnaire.questionnaire_schema import QuestionnaireSchema
from utils.helpers import (
    PUBLIC_HEALTH_INSURE_PLAN_NAME,
    PRIVATE_HEALTH_INSURE_PLAN_NAME,
    EXPAT_HEALTH_INSURE_PLAN_NAME,
    HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME,
    DENTAL_INSURE_PLAN_NAME,
    PERSONAL_LIABILITY_INSURE_PLAN_NAME,
    LEGAL_INSURE_PLAN_NAME,
    generate_recommendations,
)

questionnaire_blueprint = Blueprint(
    "questionnaire_blueprint", __name__, url_prefix="/api/v1/questionnaire"
)


@questionnaire_blueprint.route("/process", methods=["POST"])
@jwt_required
@validate_json_request(request)
@validate_schema(request, QuestionnaireSchema())
def submit_questionnaire():
    print(get_jwt_identity())
    """ This route handles questionnaire submission  """
    # Run a computation of which insurance plan should be suitable based on their occupation and children count
    data = QuestionnaireSchema().dump(request.get_json())
    has_children = data.get("has_children")
    children_count = data.get("children_count")
    occupation = data.get("occupation")
    recomendation_data = None
    default_recomendation = None

    all_plans = Plans.query.all()

    if has_children and occupation == "Employed":
        recomendation_data = {
            "highly_recommended": generate_recommendations(
                all_plans,
                (PUBLIC_HEALTH_INSURE_PLAN_NAME, HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME),
            ),
            "recommended": generate_recommendations(
                all_plans,
                (DENTAL_INSURE_PLAN_NAME, PERSONAL_LIABILITY_INSURE_PLAN_NAME),
            ),
            "least_recommended": generate_recommendations(
                all_plans,
                (
                    PRIVATE_HEALTH_INSURE_PLAN_NAME,
                    EXPAT_HEALTH_INSURE_PLAN_NAME,
                    LEGAL_INSURE_PLAN_NAME,
                ),
            ),
        }

    if children_count <= 2 and occupation == "Student":
        recomendation_data = {
            "highly_recommended": generate_recommendations(
                all_plans,
                (PUBLIC_HEALTH_INSURE_PLAN_NAME),
            ),
            "recommended": generate_recommendations(
                all_plans, (DENTAL_INSURE_PLAN_NAME)
            ),
            "least_recommended": generate_recommendations(
                all_plans, (HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME)
            ),
        }

    if children_count <= 3 and occupation == "Self-employed":
        recomendation_data = {
            "highly_recommended": generate_recommendations(
                all_plans,
                (PUBLIC_HEALTH_INSURE_PLAN_NAME, HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME),
            ),
            "recommended": generate_recommendations(
                all_plans,
                (
                    HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME,
                    PERSONAL_LIABILITY_INSURE_PLAN_NAME,
                ),
            ),
            "least_recommended": generate_recommendations(
                all_plans,
                (
                    PRIVATE_HEALTH_INSURE_PLAN_NAME,
                    DENTAL_INSURE_PLAN_NAME,
                    LEGAL_INSURE_PLAN_NAME,
                ),
            ),
        }

    if not recomendation_data:
        default_recomendation = {
            "highly_recommended": generate_recommendations(
                all_plans,
                (PUBLIC_HEALTH_INSURE_PLAN_NAME,),
            ),
            "recommended": generate_recommendations(
                all_plans,
                (HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME),
            ),
            "least_recommended": generate_recommendations(
                all_plans,
                (
                    DENTAL_INSURE_PLAN_NAME,
                    LEGAL_INSURE_PLAN_NAME,
                ),
            ),
        }
    final_recommendation = recomendation_data or default_recomendation
    # Set Recommentdation for the user
    redis_client.set(
        f"recommendation:{get_jwt_identity().get('id')}",
        json.dumps(final_recommendation),
    )
    return {
        "message": "Here is your recommendation",
        "data": final_recommendation,
        "status": "success",
    }, 200


@questionnaire_blueprint.route("/myrecommendations")
@jwt_required
def retrieve_recommendations():
    my_recommendations = redis_client.get(
        f"recommendation:{get_jwt_identity().get('id')}",
    )

    if not my_recommendations:
        return {
            "message": "You dont have any recommendation at this time",
            "status": "failed",
        }, 404

    return {
        "message": "Here is your recommendation",
        "data": json.loads(my_recommendations.decode("utf8")),
        "status": "success",
    }, 200
