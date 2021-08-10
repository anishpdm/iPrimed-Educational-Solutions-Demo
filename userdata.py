# CRUD = CREATE RETRIEVE UPDATE DELETE

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")   # Establishing a Connection
# mydatabase = client['StudentDb']  # Database
# collection_name = mydatabase['students']   # Collection

# client = pymongo.MongoClient(
#     "mongodb+srv://anish:anish@cluster0.5mwqr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydatabase = client['StudentDb']

collection_name = mydatabase['students']

result = collection_name.update_one({"rollno": "12"}, {"$set": {"name": "Ramu", "admno":354}})
# print(result.updated_count)
# studnetlist=[]
# # print(result)
# for i in result:
    
#     studnetlist.append(i)

# print(studnetlist)
# getName=input("Enter a name : ")
# getRoll=input("Enter a roll number : ")
# getAdmno=input("Enter a Admission number : ")
# getCollege = input("Enter College name : ")

# data = {"name": getName, "rollno": getRoll, "admno": getAdmno, "college": getCollege}

# result = collection_name.insert_one(data)

# print(result.inserted_id)
