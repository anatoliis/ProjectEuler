#!/usr/bin/env pypy

paths = [1] * 20
for i in xrange(20):
	for j in xrange(i):
		paths[j] += paths[j-1]
	paths[i] = 2 * paths[i-1]

print 'result: %s' % paths[-1]