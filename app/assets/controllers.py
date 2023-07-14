from fastapi import APIRouter

from app.assets.services import AssetService
from app.repositories.asset import AssetRepository

asset_router = APIRouter(prefix='/assets')


@asset_router.get('/')
async def get_assets():
    assets = await AssetService(AssetRepository()).get_assets()
    return assets
