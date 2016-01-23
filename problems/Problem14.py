#!/usr/bin/env pypy

def cached(f):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return wrapper

@cached
def chain_length(number):
	if number == 1: return 1
	if number % 2 == 0:
		next_number = number / 2
	else:
		next_number = number * 3 + 1
	return 1 + chain_length(next_number)

maximum = 0
longest = 0
for n in xrange(999999		, 0, -1):
	length = chain_length(n)
	if length > maximum:
		maximum = length
		longest = n

print 'result: %s' % longest, maximum
