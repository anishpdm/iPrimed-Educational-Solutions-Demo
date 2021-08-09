import csv,json
myfile='student.csv'
jsonfilePath='student.json'
student_list=[]
# **** Convert CSV to List
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.reader(f)
    for data in dataReader:
        student_list.append(data)

# **** Convert List to JSON
student_list_json=json.dumps(student_list)

with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(student_list_json)