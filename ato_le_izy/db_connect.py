import pymongo

DB_HOST = "localhost"
DB_PORT = 27017
client = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
db = client.ecole
