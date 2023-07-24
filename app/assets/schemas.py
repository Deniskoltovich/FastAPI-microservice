from decimal import Decimal

from pydantic import BaseModel, Field


class AssetSchema(BaseModel):
    name: str = Field(max_length=64)

    current_price: Decimal = Field(ge=0, max_digits=11, decimal_places=2)
