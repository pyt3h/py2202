
import MySQLdb
db_server = "103.124.94.100"
db_username = "admin"
db_password = "abc@123"
db_name = "py2202"
db = MySQLdb.connect(db_server, db_username, db_password, db_name, charset='utf8')
cursor = db.cursor()

cursor.execute("SELECT student_number, student_name, gpa FROM student WHERE gpa >= %s", [7.0])
                                
results = cursor.fetchall()

for record in results:
    student_number, student_name, gpa = record
    print(student_number, student_name, gpa)
    
db.close()