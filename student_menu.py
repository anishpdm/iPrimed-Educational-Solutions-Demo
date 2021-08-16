import pymongo
import valmodule
import dao_layer
studentlist = []
class Students:
    pass

while True:
    print("\n1. Add Students")
    print("\n2. Search Students")
    print("\n3. Update Students")
    print("\n4. Delete Students")
    print("\n5. View student count of each Branch")
    print("\n6. View All students ")
    print("\n7. EXIT")
    ch = int(input("Enter a Choice ? "))
    
    if (ch == 1):
        name=input("\nEnter name ? ")
        rollno=input("\nEnter Rollno ? ")
        branch = input("\nEnter Branch ? ")
        mydict = {"name": name, "rollno": rollno, "branch": branch,"del_status":0}
        if (valmodule.validate(rollno)):
            
            studentlist.append(mydict)
            dao_layer.collection_name.insert_many(studentlist)
            studentlist.clear()
        else:
            print("Invalid Roll no")
    if (ch == 2):
        name = input("\nEnter name ? ")
        result = dao_layer.collection_name.find(
            {"$and": [{"name": name}, {"del_status":0}]})
        for i in result:
            print(i)

    if (ch == 4):
        rollno = input("Enter the Rollno to be DELETED ?")
        dao_layer.collection_name.update_one(
            {"rollno": rollno}, {"$set": {"del_status": 1}})
                
    if (ch == 5):
        result = dao_layer.collection_name.aggregate(
            [{"$group": {"_id": "$branch", "no_of_students": {"$sum": 1}}}])
        for i in result:
            print(i)

    if (ch == 6):
        result = dao_layer.collection_name.find({"del_status": 0})
        for i in result:
            print(i)

    if (ch == 7):
        break;


                   

        
      

