from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.utils.config import Config, TestConfig
import os


def get_db_config():
    """Determines the configuration to be used depending on the environment."""
    if os.getenv("TESTING") == "True":
        print("TEST MODE: Connecting to Test Database")
        return TestConfig()
    print("PRODUCTION MODE: Connecting to Production Database")
    return Config()


class MongoDBConnection:
    """Handles MongoDB connection and database operations."""

    def __init__(self):
        self.config = get_db_config()
        try:
            self.client = MongoClient(self.config.MONGO_URI)
            self.client.admin.command('ping')
            print("Connected to MongoDB!")
        except ConnectionFailure:
            print("Failed to connect to MongoDB")
            self.client = None

    def get_db(self):
        """Get a database instance."""
        if self.client:
            return self.client[self.config.DATABASE_NAME]
        else:
            print("No database connection available")
            return None


db_connection = MongoDBConnection()
db = db_connection.get_db()
