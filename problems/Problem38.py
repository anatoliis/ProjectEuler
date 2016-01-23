#!/usr/bin/env python2

for n in xrange(9876, 9182, -1):
	number = str(n) + str(n*2)
	if sorted(number) == list('123456789'):
		break

print 'result: %s' % number
