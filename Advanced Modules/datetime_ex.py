print('-------------datetime module-------------')
import datetime
mytime = datetime.time(2,20)
print(mytime.minute)
print(mytime)

print('-------------date class-------------')
today = datetime.date.today()
print(today)
print(today.year) # Attribute of date class
print(today.ctime())

print('-------------datetime class-------------')
from datetime import datetime
mydatetime = datetime(2021,10,3, 14,20,1)
print(mydatetime)
print(mydatetime.replace(year=2020))

print('-------------date class-------------')
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
print(type(result))
print(result.days)

print('-------------datetime onbject-------------')
datetime1 = datetime(2021,10,3, 14,20)
datetime2 = datetime(2020,10,3, 12,20)
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
-------------datetime onbject-------------
365 days, 2:00:00
7200
31543200.0
'''
