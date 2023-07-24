import asyncio
import time

import async_to_sync as sync
import httpx
from celery.utils.log import get_task_logger

from app.assets.services import AssetService
from app.celery_app import celery_app
from app.repositories.asset import AssetRepository
from config.config import settings

logger = get_task_logger(__name__)


async def get_response(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response


@celery_app.task()
def parse_assets(collection: list[str]):
    api_key = settings.API_KEY
    url = settings.ASSET_PARSING_URL
    for asset_symbol in collection:
        asset_url = f'{url}&symbol={asset_symbol}&apikey={api_key}'
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_response(asset_url))

        if response.status_code == 200:
            document = response.json()
            logger.info(document)
            perform_upsert.delay(document["Global Quote"])

        time.sleep(5)


@celery_app.task()
def perform_upsert(document: dict):
    sync.coroutine(
        AssetService(AssetRepository()).update_asset_price_by_name(document)
    )
