#!/usr/bin/env pypy

from itertools import combinations_with_replacement as combinations
from itertools import count
from math import sqrt

def prime(n):
	for i in xrange(3, int(sqrt(n)) + 2, 2):
		if not n % i: return False
	return True

def get_numbers_of_primes(a, b):
	for max_number in count(1):
		for n in xrange(max_number):

			result = n ** 2 + a * n + b
			
			if result < 1 or not prime(result):
				return max_number

product = 0
longest = 0

for a, b in combinations(xrange(-999, 1000), 2):
	if not a % 2: continue
	number_of_primes = get_numbers_of_primes(a, b)
	
	if number_of_primes > longest:
		longest = number_of_primes
		product = a * b

print 'result: %s' % product