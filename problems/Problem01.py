#!/usr/bin/env pypy

print 'result: %s' % sum(x for x in xrange(1000) if not x % 3 or not x % 5)