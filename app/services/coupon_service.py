from datetime import datetime
import re
from app.models.coupon import Coupon
from app.utils.logging_config import logger


class CouponService:
    """
    Service layer for coupon-related operations.
    This class handles the business logic for adding and testing coupons.
    """

    @staticmethod
    def validate_condition(condition):
        """
        Validate the conditions of a coupon.

        Args:
            condition (dict): The conditions to validate. It can include:
                -'category': Must be one of ['food', 'furniture', 'electronics'].
                -'price_above': Must be an integer.
                -'date_in_range':Must be in the format'YYYY-MM-DD,YYYY-MM-DD'

        Raises:
            ValueError: If any condition is invalid.
        """
        if condition:
            # Validate 'category' condition
            if 'category' in condition and condition['category'] not in ['food', 'furniture', 'electronics']:
                logger.error("Invalid category in condition")
                raise ValueError(
                    "Category must be one of: food, furniture, electronics")

            # Validate 'price_above' condition
            if 'price_above' in condition and not isinstance(condition['price_above'], int):
                logger.error("Invalid price_above in condition")
                raise ValueError("price_above must be an integer")

            # Validate 'date_in_range' condition
            if 'date_in_range' in condition and not re.match(r'^\d{4}-\d{2}-\d{2},\d{4}-\d{2}-\d{2}$', condition['date_in_range']):
                logger.error("Invalid date_in_range in condition")
                raise ValueError(
                    "date_in_range must be the format'YYYY-MM-DD,YYYY-MM-DD'")

    @staticmethod
    def add_coupon(name, discount, condition):
        """
        Add a new coupon to the database after validating its conditions.

        Args:
            name (str): The name of the coupon.
            discount (str): The discount value (e.g., '10%' or '5').
            condition (dict): The conditions for the coupon (optional).

        Raises:
            ValueError: If the conditions are invalid.
        """
        logger.info(f"Adding coupon: {name}")

        CouponService.validate_condition(condition)

        Coupon.add_coupon(name, discount, condition)

    @staticmethod
    def test_coupon(coupon_name, product):
        """
        Test if a coupon is applicable to a given product.

        Args:
            coupon_name (str): The name of the coupon to test.
            product (dict): The product details, including:
                - 'name': The name of the product.
                - 'price': The price of the product.
                - 'category': The category of the product.

        Returns:
            float: The new price after applying the coupon (if applicable).
                  Returns None if the coupon is not applicable.

        Raises:
            ValueError: If the coupon is not found.
        """
        logger.info(f"Testing coupon: {coupon_name} for product: {product}")

        coupon = Coupon.get_coupon(coupon_name)
        if not coupon:
            logger.error(f"Coupon not found: {coupon_name}")
            raise ValueError("Coupon not found")

        condition = coupon.get('condition', {})
        true_conditions = 0

        if condition:
            # Check 'category' condition
            if 'category' in condition and condition['category'] == product['category']:
                true_conditions += 1

            # Check 'price_above' condition
            if 'price_above' in condition and condition['price_above'] < product['price']:
                true_conditions += 1

            # Check 'date_in_range' condition
            if 'date_in_range' in condition:
                start_date, end_date = condition['date_in_range'].split(',')
                if datetime.strptime(start_date, "%Y-%m-%d") < datetime.now() < datetime.strptime(end_date, "%Y-%m-%d"):
                    true_conditions += 1

        if not condition or true_conditions == len(condition):
            discount = coupon['discount']

            # Calculate the new price based on the discount type
            if discount.endswith('%'):
                new_price = product['price'] * (1 - int(discount[:-1]) / 100)
            else:
                new_price = product['price'] - int(discount)

            return new_price

        return None
