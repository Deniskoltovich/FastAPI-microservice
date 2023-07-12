import os
import time

import httpx
from celery.utils.log import get_task_logger

from app.assets.repositories import AssetRepository
from app.assets.services import AssetService
from app.celery_app import celery_app
from app.database import assets_collection

logger = get_task_logger(__name__)


@celery_app.task()
def parse_assets(collection: list[str]):
    api_key = os.environ.get('API_KEY')
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE'
    for asset_symbol in collection:
        asset_url = f'{url}&symbol={asset_symbol}&apikey={api_key}'
        response = httpx.get(asset_url)

        if response.status_code == 200:
            document = response.json()
            logger.info(document)
            perform_upsert.delay(document["Global Quote"])

        time.sleep(5)


@celery_app.task()
def perform_upsert(document: dict):
    AssetService(AssetRepository).update_asset_price(document)
