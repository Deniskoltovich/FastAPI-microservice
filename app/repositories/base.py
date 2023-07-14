from typing import AsyncGenerator


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
