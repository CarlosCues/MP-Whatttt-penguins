from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()

url = os.getenv('url')

db = MongoClient(url).get_database("Prueba")

def get_data(collection, filter={}, project={"_id":0}, limit=0, skip=0):
    return list(db[collection].find(filter,project).limit(limit).skip(skip))