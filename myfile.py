import csv
headerContent=["Name","Roll"]
studentData=[
    {"Name":"Anoop","Roll":23},
    {"Name":"Manu","Roll":20},
    {"Name":"Raja","Roll":31},
    {"Name":"Revathy","Roll":13},
    {"Name":"Aswathy","Roll":3},
]


if(__name__=='__main__'):
    with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headerContent)
    writer.writeheader()
    writer.writerows(studentData)    
