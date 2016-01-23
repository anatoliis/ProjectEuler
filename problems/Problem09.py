#!/usr/bin/env pypy
import time
import itertools

start = time.time()

for a, b in ((a,b) for a in xrange(1, 1001) for b in xrange(a+1, 1001)):
	c = (a**2 + b**2)**0.5
	if c <= b: continue
	if a + b + c == 1000: break

print 'result: %s' % int(a*b*c)
print time.time() - start
