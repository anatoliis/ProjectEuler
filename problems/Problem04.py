#!/usr/bin/env pypy

from itertools import permutations

def palindrome(n):
	n = str(n)
	length = len(n)
	half = length // 2
	return n[:half] == n[half:][::-1]

products = [a*b for a, b in permutations(range(100,1000),2)]
palindromes = [x for x in products if palindrome(x)]
print ('result: %s' % max(palindromes))