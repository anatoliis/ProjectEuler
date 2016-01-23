#!/usr/bin/env python2

from prime import prime_int as prime

n = 1
result = 2

while n < 2000000:
	n += 2
	if prime(n):
		result += n

print 'result: %s' % result