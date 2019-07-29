# -*- coding: utf-8 -*-
# Python's standard handle with date and time.
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
# To set a date and time
dt = datetime(2015, 5, 15, 5, 55)
print(dt)
# print out 2015-05-15 05:55:00
# In the computer time is a number of seconds. 1970. 1. 1 0:0:0 "timestamp" 0
dt.timestamp()
##
##
##
from datetime import timedelta, datetime
utc_dt =datetime.utcnow().replace(tzinfo=timezone.utc)
cl_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
Seattle_dt = utc_dt.astimezone(timezone(timedelta(hours=-7)))
print('ChangLi datetime is :', cl_dt)
print('Seattle datetime is :', Seattle_dt)


