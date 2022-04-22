import MySQLdb
db_server = "103.124.94.100"
db_username = "admin"
db_password = "abc@123"
db_name = "py2202"
db = MySQLdb.connect(db_server, db_username, db_password, db_name, charset='utf8')
cursor = db.cursor()

student_list = [
  {'student_number': '1001', 'student_name': 'Nguyen Van An', 'phone': '012345678', 'gpa': 7.5},
  {'student_number': '1002', 'student_name': 'Nguyen Van Ban', 'phone': '012345679', 'gpa': 8.0},
]

try:
    for student in student_list:
        cursor.execute(
          'INSERT INTO student(student_number, student_name, phone, gpa) VALUE(%s,%s,%s,%s)',
            (
              student['student_number'], 
              student['student_name'], 
              student['phone'], 
              student['gpa']
            )
          )
    db.commit()

except Exception as e:
    print(e)
    db.rollback()

finally:
    db.close()