#!/usr/bin/env pypy

def dividible(n):
	for i in xrange(11, 21):
		if n % i: return False
	return True

n = 20
while not dividible(n): n += 1

print 'result: %s' % n