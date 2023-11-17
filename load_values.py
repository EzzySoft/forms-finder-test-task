import json
from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client["form_templates"]
collection = db["template"]
with open("initial_values.json", "r") as json_file:
    initial_values = json.load(json_file)
    collection.insert_many(initial_values)
client.close()