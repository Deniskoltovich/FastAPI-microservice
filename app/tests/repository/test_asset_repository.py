import pytest

from app.repositories.base import AssetNotFoundError


class TestAssetRepository:
    #  Tests that get_assets method returns a list of assets
    @pytest.mark.asyncio
    async def test_get_assets_returns_list_of_assets(self, asset_repo):
        # Arrange
        await asset_repo.create({'name': 'asset1', 'current_price': 10.0})
        await asset_repo.create({'name': 'asset2', 'current_price': 20.0})
        # Act
        assets = await asset_repo.get_assets()
        # Assert
        assert len(assets) == 2
        assert assets[0]['name'] == 'asset1'
        assert assets[0]['current_price'] == 10.0
        assert assets[1]['name'] == 'asset2'
        assert assets[1]['current_price'] == 20.0

    #  Tests that upsert method updates an existing asset
    @pytest.mark.asyncio
    async def test_upsert_updates_existing_asset(self, asset_repo):

        # Act
        await asset_repo.upsert({'name': 'asset1'}, {'current_price': 20.0})
        asset = await asset_repo.get_by_name('asset1')
        # Assert
        assert asset['current_price'] == 20.0

    #  Tests that create method inserts a new asset into the database
    @pytest.mark.asyncio
    async def test_create_inserts_new_asset(self, asset_repo):

        # Act
        await asset_repo.create({'name': 'asset1', 'current_price': 10.0})
        asset = await asset_repo.get_by_name('asset1')
        # Assert
        assert asset['name'] == 'asset1'
        assert asset['current_price'] == 10.0

    #  Tests that get_assets method returns an empty list when no assets are found
    @pytest.mark.asyncio
    async def test_get_assets_returns_empty_list_when_no_assets_found(
        self, asset_repo
    ):

        # Act
        assets = await asset_repo.get_assets()
        # Assert
        assert len(assets) == 0

    #  Tests that upsert method inserts a new asset when no matching asset is found
    @pytest.mark.asyncio
    async def test_upsert_inserts_new_asset_when_no_matching_asset_found(
        self, asset_repo
    ):

        # Act
        await asset_repo.upsert({'name': 'asset1'}, {'current_price': 20.0})
        asset = await asset_repo.get_by_name('asset1')
        # Assert
        assert asset['current_price'] == 20.0

    #  Tests that update method raises an error when no matching asset is found
    @pytest.mark.asyncio
    async def test_update_raises_error_when_no_matching_asset_found(
        self, asset_repo
    ):
        # Act & Assert
        with pytest.raises(AssetNotFoundError):
            await asset_repo.update(
                {'name': 'asset10001'}, {'current_price': 20.0}
            )
