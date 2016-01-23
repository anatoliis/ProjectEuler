#!/usr/bin/env pypy

def factorial(n):
	result = 1
	for i in xrange(1, n):
		result *= i
	return result

print 'result: %s' % sum(map(int, str(factorial(100))))