from core.routes import app
import pytest

@pytest.fixture()
def app_client():
  yield app.test_client()
