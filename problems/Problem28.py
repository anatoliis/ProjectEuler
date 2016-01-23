#!/usr/bin/env pypy
edge = xrange(3, 1002, 2)
lst = [4*e**2-6*e+6 for e in edge]

print 'result: %s' % (sum(lst) + 1)