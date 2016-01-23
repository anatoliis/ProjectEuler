#!/usr/bin/env pypy

from math import sqrt

divs = 0
i = 0

while divs < 500:
	i += 1
	triangle = sum(xrange(1, i+1))
	divs = 0
	for j in xrange(int(sqrt(triangle)),0,-1):
		if triangle % j == 0:
			divs += 2
	# divs = len([1 for j in xrange(int(sqrt(triangle)),0,-1) if not triangle % j]) * 2

print 'result: %s' % triangle
