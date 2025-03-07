import pytest
from app.app import create_app
from app.models.user import User
from app.utils.config import Config
import jwt


@pytest.fixture
def client():
    """Configure Flask test client."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def mock_user(monkeypatch):
    """Mock the User.get_user function to simulate a valid user"""
    def mock_get_user(username):
        if username == "admin":
            return {"username": "admin", "password": "password"}
        return None

    monkeypatch.setattr(User, "get_user", mock_get_user)


def test_generate_token_success(client, mock_user):
    """Test that token generation works with valid identifiers."""
    response = client.post('/auth/token', json={
        "username": "admin",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.get_json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

    decoded_token = jwt.decode(
        data["access_token"], Config.SECRET_KEY, algorithms=["HS256"])
    assert decoded_token["sub"] == "admin"


def test_generate_token_invalid_credentials(client, mock_user):
    """Test that token generation fails with incorrect identifiers."""
    response = client.post('/auth/token', json={
        "username": "wronguser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.get_json() == {"error": "Invalid credentials"}


def test_generate_token_missing_fields(client):
    """Test that the API returns an error if any fields are missing."""
    response = client.post('/auth/token', json={})
    assert response.status_code == 401
