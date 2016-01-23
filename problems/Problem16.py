#!/usr/bin/env pypy

number = 2**1000
digits = map(int, str(number))
summ = sum(digits)
print 'result: %s' % summ