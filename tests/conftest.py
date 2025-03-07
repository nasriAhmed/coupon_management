from app.models.config_base import db
from app.app import create_app
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["TESTING"] = "True"


@pytest.fixture(scope="session", autouse=True)
def set_testing_env():
    """Vérifie que TESTING=True est bien activé avant les tests."""
    assert os.getenv(
        "TESTING") == "True", " TESTING n'est pas activé correctement"


@pytest.fixture(scope="module")
def test_app():
    """Crée une instance de l'application Flask pour les tests."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_client(test_app):
    """Crée un client de test Flask."""
    with test_app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def init_database():
    """Nettoie la base de test avant et après chaque session de test"""
    print("Resetting test database...")
    db["coupons"].delete_many({})
    yield
    db["coupons"].delete_many({})
    print("Test database cleaned.")
