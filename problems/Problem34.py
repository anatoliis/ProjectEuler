#!/usr/bin/env pypy
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
count_sum = lambda n: sum(factorial[int(i)] for i in str(n))

print 'result: %s' % sum(filter(lambda n: n == count_sum(n), xrange(3, 50000)))
for i in xrange(10): print count_sum(i)