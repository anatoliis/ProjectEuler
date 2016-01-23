#!/usr/bin/env pypy

def cached(f):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return wrapper

@cached
def fib(n):
	if n == 1 or n == 2: return 1
	return fib(n-1) + fib(n-2)

length, index = 0, 0
while length != 1000:
	index += 1
	length = len(str(fib(index)))

print 'result: %s' % index