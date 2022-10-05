import pymongo

if __name__ == "__main__":
    print("he PyMongo!")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['Rtz']
    collection = db['mySampleCollectionForrtz']

    # one = collection.find_one({'Name': 'Zaima'})
    # print(one)

    allDocs = collection.find({'Name': 'Rtz'}, {'Name': 1, '_id': 0}) #Here Id excluded and only name will appear
    # print(allDocs)

    for item in allDocs:
        print(item)