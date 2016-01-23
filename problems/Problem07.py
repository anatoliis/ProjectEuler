#!/usr/bin/env pypy

from math import sqrt

def prime(n):
	for i in xrange(3, int(sqrt(n))+2, 2):
		if not n % i: return False
	return True

number, index = 1, 1
while index != 10001:
	number += 2
	index += prime(number)

print 'result: %s' % number