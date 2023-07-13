from typing import Any, AsyncGenerator, List

from app.assets.schemas import AssetSchema
from app.database import assets_collection


class BaseRepository:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def find(self, filter: dict) -> AsyncGenerator:
        async for asset in self.collection.find(filter):
            yield asset

    async def create(self, document: dict):
        await self.collection.insert_one(document)

    async def update(self, filter: dict, update: dict, upsert: bool = False):
        await self.collection.update_one(
            filter, {'$set': update}, upsert=upsert
        )

    async def delete(self, filter: dict):
        await self.collection.delete_one(filter)


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
