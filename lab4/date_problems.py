#Task - 1
from datetime import datetime, date, timedelta
print(datetime.now()+timedelta(days=-5))
#Task - 2
from datetime import datetime, date, timedelta
print("Yesterday:", datetime.now()+timedelta(days=-1))
print("Today:", datetime.now())
print("Tommorow:", datetime.now()+timedelta(days=+1))
#Task - 3
from datetime import datetime, date, timedelta
def drop():
    print(datetime.now().replace(microsecond=0))

drop()
#Task - 4
from datetime import datetime, timedelta, time, date
today = datetime.today()
another_day = datetime.strptime("14 February 2024, 4:00:00", "%d %B %Y, %H:%M:%S")
new_day = (today - another_day).seconds
print(datetime.today())
print(new_day)