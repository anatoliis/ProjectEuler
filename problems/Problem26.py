#!/usr/bin/env pypy

def period(d):
	while d % 2 == 0:
		d /= 2
	while d % 5 == 0:
		d /= 5
	for k in range(1, d):
		if pow(10, k, d) == 1:
			return k
	return 0

length = 0
denominator = 1

for d in xrange(11, 1001):
	p = period(d)
	if p > length:
		length = p
		denominator = d

print 'result: %s' % denominator
