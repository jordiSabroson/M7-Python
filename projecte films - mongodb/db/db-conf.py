from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection URL
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
database = client["films"]
collection = database["films"]
