#!/usr/bin/env pypy
from itertools import count

not_pent = lambda p: ((p*24 + 1)**0.5 + 1) % 6
pentgen = lambda n: n * (n*3 - 1) / 2

def search():
	min_D = 10**7
	for j in count(1000):
		if j * 3 + 1 >= min_D: return min_D
		Pj = pentgen(j)
		for k in count(j+1):
			Pk = pentgen(k)
			D = Pk - Pj
			if D >= min_D:  break
			if not_pent(D): continue
			if not_pent(Pk + Pj): continue
			min_D = D
	
print 'result: %s' % search()