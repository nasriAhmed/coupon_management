from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
from app.controllers.auth_controller import auth_blueprint
from app.controllers.coupon_controller import coupon_blueprint

from app.utils.logging_config import logger

cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app() -> Flask:
    """
    Factory function to create and configure the Flask application.

    This function initializes the Flask app, loads configuration settings,
    registers blueprints for different parts of the app, and sets up logging.

    Returns:
        Flask: The configured Flask application instance.
    """
    # Initialize Flask
    app = Flask(__name__)

    # Activate cache for the app
    cache.init_app(app)

    # Enable CORS for API requests
    CORS(app)

    app.config.from_object('app.utils.config.Config')

    app.register_blueprint(coupon_blueprint)
    app.register_blueprint(auth_blueprint)

    logger.info(" Flask app initialized successfully.")

    # Display registered routes after initialization
    print("\n List of registered Flask routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
    print("\n")

    # Endpoint to empty cache
    @app.route('/clear_cache', methods=['POST'])
    def clear_cache():
        cache.clear()
        return jsonify({"message": "Cache cleared successfully"}), 200

    return app
