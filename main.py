import json
from datetime import datetime 
def read_file(file_name):
    return open(file_name).read()
def to_dic(read_f):
    return json.loads(read_f)
def max_person(dic_file):
    return min(dic_file, key=lambda person: datetime.fromisoformat(person["birthday"]))
d=read_file("data.json")
data=to_dic(d)
print(max_person(data))