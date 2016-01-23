#!/usr/bin/env pypy


print 'result: %s' % sum(n for n in xrange(2, 200000) if n == sum(x**5 for x in map(int, str(n))))