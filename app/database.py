import os

import motor.motor_asyncio

_mongodb = (
    f'mongodb://{os.environ.get("MONGO_HOST")}:{os.environ.get("MONGO_PORT")}'
)


client = motor.motor_asyncio.AsyncIOMotorClient(_mongodb)
database = client.db

assets_collection = database.assets
