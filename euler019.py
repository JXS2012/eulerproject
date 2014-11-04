__author__ = 'jianxinsun'
import time

start = time.time()
month_days_1 = [0,3,3,6,1,4,6,2,5,0,3,5]
month_days_2 = [0,3,4,0,2,5,0,3,6,1,4,6]
year = 1900
start_day = 1
sundays = 0
for i in range(101):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        days = 366
        this_year_month_days = [(start_day+x)%7 for x in month_days_2]
    else:
        days = 365
        this_year_month_days = [(start_day+x)%7 for x in month_days_1]
    if i == 0:
        sundays = 0
    else:
        sundays+=this_year_month_days.count(0)
    start_day = (start_day + days%7)%7
    year += 1
print time.time()-start
print sundays
