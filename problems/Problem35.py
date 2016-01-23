#!/usr/bin/env python2
import primes

def is_prime(n):
	if n < 2: return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if not n % i: return False
	return True

result = len((2,5))
for number in primes.primes_list(10**6):
	snum = str(number)
	if filter(lambda d: d in '024568', snum): continue
	rotations = {int(snum[i:] + snum[:i]) for i in xrange(len(snum))}
	result += len(rotations) == len(filter(is_prime, rotations))

print 'result: %s' % result