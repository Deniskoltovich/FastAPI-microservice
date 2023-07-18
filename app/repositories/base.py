from typing import AsyncGenerator


class AssetNotFoundError(Exception):
    pass


class BaseRepository:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def get_by_name(self, name: str) -> dict:
        return await self.collection.find_one({"name": name})  # type: ignore

    async def find(self, filter: dict) -> AsyncGenerator:
        async for asset in self.collection.find(filter):
            yield asset

    async def create(self, document: dict):
        await self.collection.insert_one(document)

    async def update(self, filter: dict, update: dict, upsert: bool = False):
        result = await self.collection.update_one(
            filter, {'$set': update}, upsert=upsert
        )

        if not result.matched_count and not upsert:
            raise AssetNotFoundError(
                f"No matching asset found for update: {filter}"
            )
