#!/usr/bin/env pypy

def cached(f):
	cache = {}
	def wrapper(n):
		if not n in cache:
			cache[n] = f(n)
		return cache[n]
	return wrapper

@cached
def abundant(n):
	divisors = set()
	for i in xrange(1, int(n**0.5)+1):
		if not n % i:
			divisors.add(i)
			divisors.add(n/i)
	divisors.remove(n)
	return sum(divisors) > n

def sum_of_abs(n):
	for i in xrange(12, n):
		if not abundant(i): continue
		if abundant(n-i): return True
	return False

print 'result: %s' % sum(n for n in xrange(1, 28124) if not sum_of_abs(n))