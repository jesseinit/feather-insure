import pytest
from admin.admin_model import Plans
from app import db


test_plans_seed = [
    {
        "id": "12a91b77-07ba-4aaa-aacb-9d56ad746e6f",
        "currency": "EUR",
        "payment_frequency": "Monthly",
        "price": 32.43,
        "created_on": "2020-12-25 15:34:00",
        "plan_name": "Dental Insurance",
    },
    {
        "id": "2f3f9bd0-85e6-4310-9382-67a5210c907b",
        "currency": "EUR",
        "payment_frequency": "Monthly",
        "price": 12.56,
        "created_on": "2020-12-25 15:34:00",
        "plan_name": "Personal Liability Insurance",
    },
    {
        "id": "68f909c3-03a7-4423-9a79-4f008cf958f5",
        "currency": "EUR",
        "payment_frequency": "Montly",
        "price": 432.54000000000002,
        "created_on": "2020-12-25 15:33:00",
        "plan_name": "Expat Health Insurance",
    },
    {
        "id": "8d42cd16-c288-4da3-859b-90f349677265",
        "currency": "EUR",
        "payment_frequency": "Anually",
        "price": 311.33999999999997,
        "created_on": "2020-12-25 15:35:00",
        "plan_name": "Legal Insurance",
    },
    {
        "id": "b780da5c-046d-43e3-80b5-fb5212052b76",
        "currency": "EUR",
        "payment_frequency": "Monthly",
        "price": 102.43000000000001,
        "created_on": "2020-12-25 15:33:00",
        "plan_name": "Private Health Insurance",
    },
    {
        "id": "d9f5e5c3-2a76-4e7d-9c8f-6f5c17e9005a",
        "currency": "EUR",
        "payment_frequency": "Monthly",
        "price": 132.53999999999999,
        "created_on": "2020-12-25 15:32:00",
        "plan_name": "Public Health Insurance",
    },
    {
        "id": "f5290747-3b25-4c5d-8d21-1bee0b0acbd3",
        "currency": "EUR",
        "payment_frequency": "Monthly",
        "price": 35.219999999999999,
        "created_on": "2020-12-25 15:34:00",
        "plan_name": "Household Content Insurance",
    },
]


@pytest.fixture()
def setup_plans():
    db.session.add_all([Plans(**data) for data in test_plans_seed])
    db.session.commit()
