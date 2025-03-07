from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import jwt
from app.utils.config import Config
from app.models.user import User

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/token', methods=['POST'])
def generate_token():
    """Generate a JWT token for authentication."""
    data = request.json
    print("data", data.get('username'), data.get('password'))
    username = data.get('username')
    password = data.get('password')

    user = User.get_user(username)
    if not user or user['password'] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
    return jsonify({"access_token": token, "token_type": "bearer"})
