class AssetService:
    def __init__(self, repository):
        self.repository = repository()

    async def get_assets(self):
        return await self.repository.get_assets()

    def update_asset_price(self, document):
        filter = {'name': document["01. symbol"]}
        document = {
            'name': document["01. symbol"],
            'current_price': document["05. price"],
        }

        self.repository.upsert(filter, document)
