from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_PASS, MONGO_USER, MONGO_URI, MONGO_APP, MONGO_DB

client = AsyncIOMotorClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_URI}/?retryWrites=true&w=majority&appName={MONGO_APP}')
# client = AsyncIOMotorClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_URI}")

db = client[MONGO_DB]
