import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client['CollegeDb']
collection_name = mydatabase['students']
