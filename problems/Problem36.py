#!/usr/bin/env pypy

palindrome = lambda n: str(n) == str(n)[::-1]
binary = lambda n: '{0:b}'.format(n)
p_list = {n for n in xrange(1, 1000000, 2) if palindrome(n) and palindrome(binary(n))}

print 'result: %s' % sum(p_list)