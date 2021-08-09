import json

studentlist=[{"name":"Anuj","roll":23},{"name":"Sidharth","roll":13}]

myjsondata=json.dumps(studentlist)

with open('test.json','w',encoding='utf-8') as f:
    f.write(myjsondata)
