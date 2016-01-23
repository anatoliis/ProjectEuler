#!/usr/bin/env pypy

def cached(f):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return wrapper

@cached
def prime(n):
	if n == 2: return True
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if not n % i: return False
	return True

def truncatable(n):
	n = str(n)
	if n[-1] in '19' or n[0] in '14689': return False
	for i in xrange(1, len(n)):
		if not prime(int(n[:i])): return False
	for i in xrange(len(n)):
		if not prime(int(n[i:])): return False
	return True

result = sum([p for p in xrange(11, 740000, 2) if truncatable(p)])
print 'result: %s' % result