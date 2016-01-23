#!/usr/bin/env python2
from itertools import permutations

def prime(n):
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if not n % i: return False
	return True

def search():
	for length in xrange(9, 0, -1):
		for n in permutations(''.join(map(str, xrange(length, 0, -1)))):
			n = int(''.join(n))
			if prime(n): return n

print 'result: %s' % search()