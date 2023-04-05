import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DB_NAME')]
collection = db[os.getenv('MONGO_DB_NAME')]

user_schema = {
    "type": "object",
    "properties": {
        '_id': {'type': 'integer'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    "required": ["_id","name", "email", "password"]
}