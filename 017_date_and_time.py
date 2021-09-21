import datetime

d = datetime.date(2021, 9, 18)
today = datetime.date.today()
print(type(today - d)) #type TIMEDELTA - kolichestvennoe vremja
t_delta = datetime.timedelta(days=30, weeks=3, minutes=34)
print(today + t_delta)

print('----------------------------------')

t = datetime.time(21, 11, 23, 99999)
print(t.hour)

print('----------------------------------')

print(datetime.time())
print(today)
print(type(d))
print(type(today))

print('----------------------------------')

print(today.year)
print(today.month)
print(today.day)
print(today.day, today.month, today.year, today.weekday())
print(datetime.date.weekday(d))
print(d.weekday())
print(today.isoweekday())

print('----------------------------------')

next_bday = datetime.date(2021, 12, 15)
til_bday = next_bday - today
print(til_bday.total_seconds())
print(type(til_bday))

print('-------------------------------------------------')

dt = datetime.datetime(2121, 9, 21, 0, 0, 0)
#dt = datetime.datetime(year=2021, month=9, day=0)
print(dt)
dt_time = dt.time()
dt_date = dt.date()
print(type(dt_date))
print(dt_date)
print(type(dt_time))
print((dt_time))

print('---------------------------')

today = datetime.datetime.now()
print(today.time())
print(today.date())
print(today.day)

print('----------------------------------')

dt3 = datetime.datetime(2121, 9, 21, 0, 0, 0)
print(dt3)
t_delta3 = datetime.timedelta(22, 11, 0, 0)
print(t_delta3)
print(dt3 - t_delta3)

print('----------------------------------')

print(today.strftime('%d.%m.%Y'))
today_str = today.strftime('%D %B %Y')
print(today_str)
print(type(today_str))

print('----------------------------------')

dt1 = '30 Mar 21'
dt2 = 'November 15, 2021'
print(dt1)
new_dt1 = datetime.datetime.strptime(dt1, '%d %b %y')
print(new_dt1)
print(type(new_dt1))
print()
print(dt2)
new_dt2 = datetime.datetime.strptime(dt2, '%B %d, %Y')
print(new_dt2)
print(type(new_dt2))



