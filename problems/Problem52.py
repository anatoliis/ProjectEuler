#!/usr/bin/env python2
n = 1
while not len({''.join(sorted(str(n*i))) for i in xrange(1,7)}) == 1:
	n += 1

print 'result: %s' % n