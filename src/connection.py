from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
import redis

load_dotenv()

def connectMongo():
    uri = os.getenv("MONGO_URI")

    client = MongoClient(uri, server_api=ServerApi('1'))

    return client[os.getenv("MONGO_CLUSTER")]

def connectRedis():
    return redis.Redis(
        host = os.getenv("REDIS_HOST"),
        port = 14785,
        decode_responses = True,
        username = "default",
        password = os.getenv("REDIS_PASSWORD")
    )