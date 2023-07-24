import os

import motor.motor_asyncio

from config.config import settings

_mongodb = settings.DATABASE_URL


client = motor.motor_asyncio.AsyncIOMotorClient(_mongodb)
database = client.db

assets_collection = database.assets
