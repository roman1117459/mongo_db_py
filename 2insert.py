
import pymongo

if __name__ == "__main__":
    print("he PyMongo!")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['Rtz'] # this is for database name
    collection = db['mySampleCollectionForrtz'] #This is for collection name

    #Insert for one single data

    # dictionary = {'name': 'Rtz', 'marks': 90}
    # collection.insert_one(dictionary)
    # dictionary2 = {'name': 'Rtza', 'marks': 94}
    # collection.insert_one(dictionary2)

    #THis is for many data
    insertThese = [
        {'_id':55, 'Name': 'Rtza', 'Location': 'Mirpur', 'Marks': 70},
        {'_id':56, 'Name': 'Ratul', 'Location': 'Mirpur', 'Marks': 50},
        {'_id':32, 'Name': 'Zaima', 'Location': 'Mirpur', 'Marks': 50},
        {'_id':42, 'Name': 'Fariya', 'Location': 'Mirpur', 'Marks': 50},
    ]

    collection.insert_many(insertThese) #For too many datas
