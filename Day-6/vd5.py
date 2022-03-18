from datetime import datetime

dt = datetime.now()
print(dt.strftime('%d-%m-%Y'))
print(dt.strftime('ngày %d, tháng %m, năm %Y, %H giờ %M phút %S'))