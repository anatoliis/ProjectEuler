#!/usr/bin/env pypy

def fibo():
	previous, current = 1, 2
	end = 4*10**6
	yield previous
	yield current
	while current <= end:
		current, previous = previous + current, current
		yield current

print 'result: %s' % sum(x for x in fibo() if not x % 2)