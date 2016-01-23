#!/usr/bin/env python2
import itertools
import primes

def conjecture(n):
	for i in xrange(int((n/2)**0.5), 0, -1):
		if primes.prime(n - 2*i**2): return True
	return False

for number in itertools.count(33, 2):
	if primes.prime(number): continue
	if not conjecture(number): break

print 'result: %s' % number