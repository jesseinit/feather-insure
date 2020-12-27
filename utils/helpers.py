from admin.admin_schema import PlansModelSchema
from typing import Dict, List
from admin.admin_model import Plans


def generate_recommendations(
    all_plans_list: List[Plans], plan_names_list: List[str]
) -> List[Dict]:
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    all_plans_list : List[Plans]
        A list of Plans(Model) instances
    plan_names_list : List[str]
        A list of plan names

    Returns
    -------
    dict
        A dictionary representing the various recommendations
    """
    return [
        PlansModelSchema().dump(plan)
        for plan in all_plans_list
        if plan.plan_name in plan_names_list
    ]


# Constants
PUBLIC_HEALTH_INSURE_PLAN_NAME = "Public Health Insurance"
PRIVATE_HEALTH_INSURE_PLAN_NAME = "Private Health Insurance"
EXPAT_HEALTH_INSURE_PLAN_NAME = "Expat Health Insurance"
HOUSE_HOLD_CONTENT_INSURE_PLAN_NAME = "Household Content Insurance"
DENTAL_INSURE_PLAN_NAME = "Dental Insurance"
PERSONAL_LIABILITY_INSURE_PLAN_NAME = "Personal Liability Insurance"
LEGAL_INSURE_PLAN_NAME = "Legal Insurance"
