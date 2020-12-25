from admin.admin_schema import PlansModelSchema


def generate_recommendations(all_plans_list, plan_names_list):
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
