from pymongo import MongoClient
from config import MONGODB_URL, DB_NAME

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]