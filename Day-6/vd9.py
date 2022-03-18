# Một phim được chiếu tại 1 rạp vào 8h30 tối thứ 4 và 3h chiều T7
# In ra thời gian của các buổi chiếu tiếp theo
from datetime import date, timedelta, datetime

schedules = [
    {"dow": 2, "hour": 20, "minute": 30},
    {"dow": 5, "hour": 15, "minute": 0},
]

def get_next_show(dow, hour, minute):
    d = date.today() + timedelta(days=1)
    while d.weekday() != dow:
        d += timedelta(days=1)
    return datetime(d.year, d.month, d.day, hour, minute, 0)

for s in schedules:
    print(get_next_show(s['dow'], s['hour'], s['minute']))