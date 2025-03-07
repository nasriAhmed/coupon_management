from app.models.config_base import db


class Coupon:
    """Coupon model for MongoDB operations."""
    collection = db['coupons']

    @staticmethod
    def add_coupon(name, discount, condition):
        """Add a new coupon to the database."""
        coupon_data = {
            "name": name,
            "discount": discount,
            "condition": condition
        }
        Coupon.collection.insert_one(coupon_data)

    @staticmethod
    def get_coupon(name):
        """Retrieve a coupon by its name."""
        return Coupon.collection.find_one({"name": name})
