from app.services.coupon_service import CouponService
from app.models.coupon import Coupon
from app.security.validation import Product


def test_add_coupon(init_database):
    """Test adding a coupon."""
    CouponService.add_coupon("coupon_1", "10%", {"category": "food"})
    coupon = Coupon.get_coupon("coupon_1")
    assert coupon is not None
    assert coupon["discount"] == "10%"


def test_test_coupon(init_database):
    """Test applying a coupon."""
    CouponService.add_coupon("coupon_1", "10%", {"category": "food"})
    product = Product(name="cake", price=60, category="food")
    new_price = CouponService.test_coupon("coupon_1", product.dict())
    assert new_price == 54.0
