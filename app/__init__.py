from flask import Flask
from app.controllers.coupon_controller import coupon_blueprint
from app.utils.logging_config import logger


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object('app.utils.config.Config')

    # Register blueprints
    app.register_blueprint(coupon_blueprint)

    logger.info("Flask app initialized successfully.")
    return app
