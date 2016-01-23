#!/usr/bin/env python2
import time
import primes as prime

cache = {}
def factors(n):
	if n in cache: return cache[n]
	primes = []
	rest = n
	for p in prime.primes_half(n+1):
		while not rest % p:
			primes.append(p)
			rest /= p
	primes = set(primes)
	cache[n] = len(primes)
	return len(primes)

start = time.time()

n = 114000
length = 4
while True:
	# if not n % 100: print n
	if factors(n) != length:
		n += 1
		continue
	if factors(n+1) != length:
		n += 2
		continue
	if factors(n+2) != length:
		n += 3
		continue
	if factors(n+3) != length:
		n += 4
		continue
	break

print 'result: %s' % n
print time.time() - start