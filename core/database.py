from pymongo import MongoClient

def get_db():
    mongo_uri = "mongodb://scluser:password@localhost:27017/sclmgmt"
    client = MongoClient(mongo_uri)
    db = client.get_database()
    return db
