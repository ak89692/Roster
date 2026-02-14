from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]
user = {"name": "Alice", "age": 25}
result = collection.delete_one(user)