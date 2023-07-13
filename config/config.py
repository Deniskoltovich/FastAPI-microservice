import os

from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    API_KEY: str
    ASSET_PARSING_URL: str

    BROKER_REDIS_URL: str
    REDIS_PORT: int
    DATABASE_URL: str

    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str

    KAFKA_ADVERTISED_HOST_NAME: str
    KAFKA_BROKER_ID: int
    KAFKA_ZOOKEEPER_CONNECT: str
    KAFKA_ADVERTISED_LISTENERS: str
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: str
    KAFKA_INTER_BROKER_LISTENER_NAME: str
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: int
    KAFKA_PORTS: str

    ZOOKEEPER_CLIENT_PORT: int
    ZOOKEEPER_TICK_TIME: int
    ZOOKEEPER_PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
