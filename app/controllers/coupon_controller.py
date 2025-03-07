from flask import Blueprint, request, jsonify
from app.services.coupon_service import CouponService
from app.security.auth import token_required

# Create a Blueprint for coupon-related routes
coupon_blueprint = Blueprint('coupon', __name__)


@coupon_blueprint.route('/add_coupon', methods=['POST'])
@token_required
def add_coupon():
    """
    Endpoint to add a new coupon.

    This endpoint requires a valid JWT token for authentication.
    It expects a JSON payload with the following fields:
        - name (str): The name of the coupon.
        - discount (str): The discount value (e.g., '10%' or '5').
        - condition (dict, optional): The conditions for the coupon.

    Returns:
        - On success: A JSON response with success msg & HTTP status code 201
        - On error: A JSON response with error msg & HTTP status code 400
    """
    data = request.json

    try:
        # Call the CouponService to add the coupon
        CouponService.add_coupon(
            data['name'], data['discount'], data.get('condition', {}))

        return jsonify({"message": "Coupon added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@coupon_blueprint.route('/test_coupon', methods=['POST'])
@token_required
def test_coupon():
    """
    Endpoint to test if a coupon is applicable to a product.

    This endpoint requires a valid JWT token for authentication.
    It expects a JSON payload with the following fields:
        - coupon_name (str): The name of the coupon to test.
        - product (dict): The product details, including:
            - name (str): The name of the product.
            - price (float): The price of the product.
            - category (str): The category of the product.

    Returns:
        - If applicable: A JSON response with the new price
            and HTTP status code 200.
        - If not applicable: A JSON response with a message
            and HTTP status code 200.
        - On error: A JSON response with an error message
            and HTTP status code 400.
    """
    data = request.json

    try:
        # Call the CouponService to test the coupon
        new_price = CouponService.test_coupon(
            data['coupon_name'], data['product'])

        if new_price is not None:
            return jsonify({"new_price": new_price}), 200
        else:
            return jsonify({"message": "Coupon not applicable"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
