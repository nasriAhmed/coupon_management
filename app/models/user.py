class User:
    """Mock user model for authentication."""
    @staticmethod
    def get_user(username):
        """Retrieve a user by username (mock implementation)."""
        users = {
            "admin": {"username": "admin", "password": "password"}
        }
        return users.get(username)
