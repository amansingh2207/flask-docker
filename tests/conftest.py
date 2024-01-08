import pytest
from app import create_app

@pytest.fixture(scope='module')
def test_app():
    """
    Create a Flask app instance for tests.
    """
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    yield app
