import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

connected = False
def connect_to_mongodb():
    global connected
    if not connected:
        try:
            # Create a MongoClient object and specify the connection URL
            client = MongoClient(MONGO_URI)
            global db

            # Access the database
            db = client['zenme']

            # Return the collection object
            connected = True
            # print("Connected to MongoDB :", db)
            print("Connected to MongoDB")

            return db

        except Exception as e:
            print(f"Error connecting to MongoDB: {str(e)}")
    else:
        print("Already connected to MongoDB")
        return db


def mongo_collection(collection_name):
    db = connect_to_mongodb()
    collection = db[collection_name]
    return collection