from datetime import datetime, timedelta
now = datetime.now()
this_time_next_week = now + timedelta(days=7)
print(this_time_next_week)

from datetime import datetime, timedelta
now = datetime.now()
end_time = now + timedelta(hours=3)
print(end_time)