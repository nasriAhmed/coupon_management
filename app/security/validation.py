from pydantic import BaseModel, Field, validator
from typing import Optional
import re


class CouponCreate(BaseModel):
    """Schema for creating a new coupon."""
    name: str = Field(..., example="coupon_1", min_length=1, max_length=50)
    discount: str = Field(..., example="10%", min_length=1, max_length=10)
    condition: Optional[dict] = Field(
        default=None, example={"category": "food"})

    @validator('discount')
    def validate_discount(cls, value):
        """Validate the discount format."""
        if not (value.endswith('%') or value.isdigit()):
            raise ValueError(
                "Discount must be a percentage (e.g., '10%') or a fixed amount (e.g., '5')")
        return value

    @validator('condition')
    def validate_condition(cls, value):
        """Validate the coupon conditions."""
        if value:
            if 'category' in value and value['category'] not in ['food', 'furniture', 'electronics']:
                raise ValueError(
                    "Category must be one of: food, furniture, electronics")
            if 'price_above' in value and not isinstance(value['price_above'], int):
                raise ValueError("price_above must be an integer")
            if 'date_in_range' in value and not re.match(r'^\d{4}-\d{2}-\d{2},\d{4}-\d{2}-\d{2}$', value['date_in_range']):
                raise ValueError(
                    "date_in_range must be in the format 'YYYY-MM-DD,YYYY-MM-DD'")
        return value


class Product(BaseModel):
    """Schema for testing a coupon against a product."""
    name: str = Field(..., example="cake", min_length=1, max_length=50)
    price: float = Field(..., example=10.0, gt=0)
    category: str = Field(..., example="food", min_length=1, max_length=50)


class Token(BaseModel):
    """Schema for JWT token."""
    access_token: str = Field(...,
                              example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = Field(..., example="bearer")
