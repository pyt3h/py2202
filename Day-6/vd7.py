# In ra ngày tháng năm của ngày chủ nhật sắp tới

from datetime import date, timedelta

d = date.today() + timedelta(days=1)

while d.weekday() != 6:
    d += timedelta(days=1)

print(d)