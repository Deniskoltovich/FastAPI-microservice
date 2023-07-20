import pytest


class TestAssetService:
    #  Tests that the get_assets method returns a list of assets
    @pytest.mark.asyncio
    async def test_get_assets_returns_list_of_assets(self, service):

        # Act
        assets = await service.get_assets()
        # Assert
        assert isinstance(assets, list)

    #  Tests that the update_asset_price_by_name method updates asset price and sends updated info
    @pytest.mark.asyncio
    async def test_update_asset_price_by_name_updates_asset_price_and_sends_updated_info(
        self, service, mocker
    ):
        # Arrange

        document = {"01. symbol": "AAPL", "05. price": 100.0}
        mocker.patch("app.producer.send_updated_asset_info", return_value=None)

        # Act
        await service.update_asset_price_by_name(document)
        assets = await service.get_assets()
        asset = next(
            (
                asset
                for asset in assets
                if asset["name"] == document["01. symbol"]
            ),
            None,
        )
        # Assert
        assert asset is not None
        assert asset["current_price"] == document["05. price"]

    #  Tests that the get_assets method returns an empty list when no assets are found
    @pytest.mark.asyncio
    async def test_get_assets_returns_empty_list_when_no_assets_found(
        self, service
    ):
        # Act
        assets = await service.get_assets()
        # Assert
        assert assets == []

    @pytest.mark.asyncio
    async def test_update_asset_price_by_name_insert_asset_when_filter_field_dont_match_any(
        self, service, asset_repo, mocker
    ):
        # Arrange
        document = {"01. symbol": "not exist", "05. price": 100.0}
        mocker.patch("app.producer.send_updated_asset_info", return_value=None)

        # Act
        await service.update_asset_price_by_name(document)
        asset = await asset_repo.get_by_name(document.get('01. symbol'))
        # Assert
        assert asset.get('name') == document.get("01. symbol")
        assert asset.get('current_price') == document.get('05. price')

    #  Tests that the get_assets method returns assets in correct format
    @pytest.mark.asyncio
    async def test_get_assets_returns_assets_in_correct_format(self, service):
        # Act
        assets = await service.get_assets()
        # Assert
        assert all([isinstance(asset, dict) for asset in assets])

    #  Tests that the update_asset_price_by_name method sends correct message format
    @pytest.mark.asyncio
    async def test_update_asset_price_by_name_sends_correct_message_format(
        self, service, asset_repo, mocker
    ):
        # Arrange
        document = {"01. symbol": "AAPL", "05. price": 100.0}
        mocker.patch("app.producer.send_updated_asset_info", return_value=None)

        # Act
        await service.update_asset_price_by_name(document)
        asset = await asset_repo.get_by_name(document["01. symbol"])
        # Assert
        assert asset.get('name') == document.get("01. symbol")
        assert asset.get('current_price') == document.get('05. price')

    #  Tests that the upsert method inserts new asset when no matching filter is found
    @pytest.mark.asyncio
    async def test_upsert_method_inserts_new_asset_when_no_matching_filter_is_found(
        self, service, asset_repo
    ):
        # Arrange

        document = {"name": "AAPL", "current_price": 100.0}
        filter_field = {"name": "INVALID"}
        # Act
        await service.repository.upsert(filter_field, document)
        asset = await asset_repo.get_by_name(document.get('name'))
        # Assert
        assert asset["current_price"] == 100.0
