#!/usr/bin/env pypy

def divisors_sum(n):
	divisors = set()
	for i in xrange(1, int(n**0.5)+1):
		if not n % i:
			divisors.add(i)
			divisors.add(n/i)
	if n > 1: divisors.remove(n)
	return sum(divisors)

result = 0
for number in xrange(1, 10001):
	s = divisors_sum(number)
	if number == s or divisors_sum(s) != number: continue
	result += number

print 'result:', result
print divisors_sum(10000)