#!/usr/bin/env pypy
import itertools

solutions = {}

for a, b in itertools.combinations(xrange(100, 1000), 2):
	c = (a**2 + b**2)**0.5
	if not int(c) == c: continue
	p = a + b + int(c)
	if p > 1000: continue
	if not p in solutions: solutions[p] = 1
	else: solutions[p] += 1

print 'result: %s' % max(solutions, key=lambda n: solutions[n])