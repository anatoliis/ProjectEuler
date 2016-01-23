#!/usr/bin/env python2

from math import sqrt
from prime import prime_int as prime

number = 600851475143
start = int(sqrt(number))

if not start % 2: start += 1
for n in xrange(start, 0, -2):
	if not prime(n): continue
	if not number % n: break

print 'result: %s' % n