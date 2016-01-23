#!/usr/bin/env pypy

from itertools import permutations, islice
a = permutations(map(str, xrange(10)), 10)
b = islice(a, 999999, 1000000)
print 'result: %s' % ''.join(*b)