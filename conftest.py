import pytest
from app import create_app, db

pytest_plugins = ["tests.user_entity_tests.user_fixtures"]


@pytest.fixture(scope="function")
def client():
    test_app = create_app("test")
    testing_client = test_app.test_client()

    with test_app.app_context():
        db.create_all()
        yield testing_client
        db.session.close()
        db.drop_all()
