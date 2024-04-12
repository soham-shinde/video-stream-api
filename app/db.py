from pymongo import MongoClient

def get_database_client():
    client = MongoClient("mongodb+srv://vitepen266:8haGD2QnI68v1m0W@cluster0.cahjjep.mongodb.net/")
    return client["video-stream"]
