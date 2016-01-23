#!/usr/bin/env pypy

def leap(y):
	if y % 4: return False
	if y % 100: return True
	if y % 400: return False
	return True

def next_day(d,m,y,day_of_week):
	day_of_week = (day_of_week + 1) if (day_of_week < 7) else 1
	days = (None,31,28,31,30,31,30,31,31,30,31,30,31)[m] + (leap(y) and m == 2)
	if d < days: return d + 1, m, y, day_of_week
	if m == 12: return 1, 1, y + 1, day_of_week
	return 1, m + 1, y, day_of_week

start = (1,1,1901,2) # 2 is Tuesday
end = (31,12,2000)

date = start
sundays = 0
while date[:-1] != end:
	date = next_day(*date)
	if date[0] == 1 and date[-1] == 7:
		sundays += 1

print 'result:', sundays