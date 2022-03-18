# Tìm ngày cách N ngày làm việc so với hôm nay

from datetime import date, timedelta

d = date.today()
N = 10

while N > 0:
    d += timedelta(days=1)
    if d.weekday() not in [5,6]:
        N -= 1

print(d)
