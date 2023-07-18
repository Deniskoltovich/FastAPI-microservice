import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer

from config.config import settings


async def send_updated_asset_info(message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=settings.BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        await producer.send_and_wait(
            'Assets', json.dumps(message).encode('utf-8')
        )
        logging.info(f'Message sent: {message}')
    finally:
        await producer.stop()
