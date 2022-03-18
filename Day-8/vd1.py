
import json

student_list = [
  {'name': 'Nguyễn Văn A', 'date-of-birth': '01/01/2000', 'address': 'Hà Nội'},
  {'name': 'Nguyễn Văn B', 'date-of-birth': '02/02/2000', 'address': 'TP.HCM'},
]

student_list_json = json.dumps(student_list) # Chuyển từ Python ➝ JSON
print(student_list_json)

student_list2 = json.loads(student_list_json) # Chuyển từ JSON ➝ Python

for st in student_list2:
  print(st['name'], st['date-of-birth'], st['address'])