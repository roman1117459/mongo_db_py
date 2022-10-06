import pymongo

if __name__ == "__main__":
    print("he PyMongo!")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    allDatabases = client.list_database_names()
    print(allDatabases)
    col = client['Rtz']
    print(col.list_collection_names())
