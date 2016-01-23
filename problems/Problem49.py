#!/usr/bin/env python2
import time
from itertools import *

def prime(n):
	if n < 3: return n == 2
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if not n % i: return False
	return True

def find():
	for pack in combinations_with_replacement(xrange(10), 4):
		perms = {int('%s'*4 % n) for n in permutations(pack, 4)}
		print len(perms)
		perms = [n for n in perms if n > 1000 and prime(n)]
		if len(perms) < 3: continue
		# print len(perms)
		for first, second in ((f, s) for f in perms for s in perms if s > f):
			third = second * 2 - first
			if third in perms and first != 1487:
				return (first, second, third)

print 'result: %s%s%s' % find()