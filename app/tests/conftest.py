import asyncio

import pytest
from mongomock_motor import AsyncMongoMockClient

from app.assets.services import AssetService
from app.repositories.asset import AssetRepository
from app.repositories.base import BaseRepository


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def collection():
    collection = AsyncMongoMockClient()['tests']['test-1']
    return collection


@pytest.fixture
def asset_repo(collection):
    asset_repo = AssetRepository(collection)
    return asset_repo


@pytest.fixture
def base_repo(collection):
    base_repo = BaseRepository(collection)
    return base_repo


@pytest.fixture()
def service(asset_repo):
    service = AssetService(asset_repo)
    return service
