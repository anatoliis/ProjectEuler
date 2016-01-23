#!/usr/bin/env pypy

def d(pos):
	length, ln, number = 0, 1, 1
	while length + ln < pos:
		length += ln
		number += 1
		ln = len(str(number))
	return int(str(number)[pos-length-1])

print 'result: %s' % reduce(lambda x,y: x*y, (d(10**i) for i in xrange(7)))