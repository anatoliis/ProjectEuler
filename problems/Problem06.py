#!/usr/bin/env pypy

sum_of_squares = sum(x**2 for x in xrange(101))
square_of_sums = sum(xrange(101))**2

print 'result: %s' % (square_of_sums - sum_of_squares)