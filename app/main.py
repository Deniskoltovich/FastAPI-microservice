import json

from bson import json_util
from fastapi import FastAPI

from app.assets.controllers import asset_router
from app.assets.tasks import parse_assets
from app.database import assets_collection

app = FastAPI()
app.include_router(asset_router)
