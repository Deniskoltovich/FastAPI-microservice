from app.producer import send_updated_asset_info
from app.repositories.asset import AssetRepository


class AssetService:
    def __init__(self, repository: AssetRepository):
        self.repository = repository

    async def get_assets(self):
        return await self.repository.get_assets()

    async def update_asset_price_by_name(self, document: dict) -> None:
        filter_field = {'name': document["01. symbol"]}
        document = {
            'name': document["01. symbol"],
            'current_price': document["05. price"],
        }

        await self.repository.upsert(filter_field, document)
        await send_updated_asset_info(document)
