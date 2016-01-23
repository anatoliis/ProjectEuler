#!/usr/bin/env python2

products = set()
for m1 in xrange(2, 100):
	if m1 % 5 == 0 or m1 % 10 == 1: continue
	limits = xrange(102, 200) if m1 > 9 else xrange(1002, 2000)
	for m2 in limits:
		if m2 % 5 == 0 or m2 % 10 == 1: continue
		prod = m1 * m2
		digits = [d for d in str(m1) + str(m2) + str(prod)]
		if len(set(digits)) != len(digits): continue
		if ''.join(sorted(digits)) != '123456789':
			continue
		products.add(prod)

print 'result: %s' % sum(products)