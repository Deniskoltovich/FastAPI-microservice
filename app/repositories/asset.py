from typing import Any, List

from app.assets.schemas import AssetSchema
from app.database import assets_collection
from app.repositories.base import BaseRepository


class AssetRepository(BaseRepository):
    def __init__(self, collection=assets_collection) -> None:
        super().__init__(collection)

    async def get_assets(self) -> List[dict[str, Any]]:
        # assets = await self.find({})
        return [
            AssetSchema(**asset).model_dump() async for asset in self.find({})
        ]

    async def upsert(self, filter: dict, doc: dict):
        await self.update(filter, doc, upsert=True)
