from decimal import Decimal

import pytest

from app.assets.schemas import AssetSchema


class TestAssetSchema:
    #  Tests that an AssetSchema instance can be created with valid name and current_price
    def test_valid_asset(self):
        asset = AssetSchema(name='Bitcoin', current_price=Decimal('50000.00'))
        assert asset.name == 'Bitcoin'
        assert asset.current_price == Decimal('50000.00')

    #  Tests that the name and current_price attributes of an AssetSchema instance can be accessed
    def test_access_name_and_current_price(self):
        asset = AssetSchema(name='Ethereum', current_price=Decimal('3000.00'))
        assert asset.name == 'Ethereum'
        assert asset.current_price == Decimal('3000.00')

    #  Tests that an AssetSchema instance cannot be created with a name longer than 64 characters
    def test_long_name(self):
        with pytest.raises(ValueError):
            AssetSchema(name='a' * 65, current_price=Decimal('100.00'))

    #  Tests that an AssetSchema instance cannot be created with a negative current_price
    def test_negative_current_price(self):
        with pytest.raises(ValueError):
            AssetSchema(name='Dogecoin', current_price=Decimal('-0.01'))

    #  Tests that an AssetSchema instance can be created with a current_price of 0
    def test_current_price_zero(self):
        asset = AssetSchema(name='Test Asset', current_price=Decimal('0'))
        assert asset.name == 'Test Asset'
        assert asset.current_price == Decimal('0')

    #  Tests that an AssetSchema instance can be created with a current_price of 999999999.99
    def test_current_price_max(self):
        asset = AssetSchema(
            name='Test Asset', current_price=Decimal('999999999.99')
        )
        assert asset.name == 'Test Asset'
        assert asset.current_price == Decimal('999999999.99')
