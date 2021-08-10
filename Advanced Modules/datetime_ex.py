import os
import datetime as dt
from datetime import time
from datetime import datetime
from datetime import date
os.system('cls')

print('-------------datetime module-------------')
mytime = time(2,20,20)
print(mytime.minute)
print(mytime)

print('-------------date class-------------')
today = date.today()
print(today)
print(today.year) # Attribute of date class
print(today.ctime())

print('-------------datetime class-------------')
mydatetime = datetime(2021,10,3,14,20,1,200)
print(mydatetime)
print(mydatetime.replace(year=2020))

curr_time = datetime.now().replace(microsecond=0)
print(f"curr_time: {curr_time}")

print('-------------date class-------------')
date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
print(type(result))
print(result.days)

print('-------------datetime object-------------')
datetime1 = datetime(2021,10,3,14,20)
datetime2 = datetime(2020,10,3,12,20)
mydiff = datetime1 - datetime2
print(mydiff)
print(mydiff.seconds)
print(mydiff.total_seconds())

'''
-------------datetime module-------------
20
02:20:00
-------------date class-------------
2021-05-17
2021
Mon May 17 00:00:00 2021
-------------datetime class-------------
2021-10-03 14:20:01
2020-10-03 14:20:01
-------------date class-------------
<class 'datetime.timedelta'>
365
-------------datetime object-------------
365 days, 2:00:00
7200
31543200.0
'''
