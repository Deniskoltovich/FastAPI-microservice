from app.assets.schemas import AssetSchema
from app.database import assets_collection


class AssetRepository:
    def __init__(self):
        self.collection = assets_collection

    async def get_assets(self):
        return [
            AssetSchema(**asset).model_dump()
            async for asset in self.collection.find()
        ]

    async def upsert(self, filter, doc):
        return self.collection.update_one(filter, {'$set': doc}, upsert=True)
