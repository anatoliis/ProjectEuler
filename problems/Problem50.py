#!/usr/bin/env python2
from primes import primes_list, prime

def find():
    primes = primes_list(10**4)
    for length in xrange(1000, 0, -1):
        first = 0
        while True:
            summ = sum(primes[first:first+length])
            # print summ
            if summ >= 10**6: break
            if prime(summ): return summ
            first += 1

print 'result: %s' % find()
