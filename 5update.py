import pymongo

if __name__ == "__main__":
    print("he PyMongo!")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['Rtz']
    collection = db['mySampleCollectionForrtz']
    #
    # #Delete one
    #
    # rec = {"Name": "Rtz"}
    # collection.delete_one(rec)

    #Delete Many
    rec = {"Name": "Rtza"}
    up = collection.delete_many(rec)
    print(up.deleted_count)

