import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/coupon_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    DATABASE_NAME = "coupon_db"


class TestConfig(Config):
    """Configuration for testing."""
    MONGO_URI = os.getenv(
        "TEST_MONGO_URI", "mongodb://localhost:27017/test_coupon_db")
    DATABASE_NAME = "test_coupon_db"
    SECRET_KEY = os.getenv("SECRET_KEY", "test_secret_key")
