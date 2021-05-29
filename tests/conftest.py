import server as flask_app
import sys
import pytest

sys.path.insert(0, './')
sys.path.insert(0, './src')


@pytest.fixture
def app():
    flask_app.connex_app.app.testing = True
    yield flask_app.connex_app.app


@pytest.fixture
def client(app):
    return app.test_client()
