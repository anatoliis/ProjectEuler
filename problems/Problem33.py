#!/usr/bin/env pypy

result = []
for num in xrange(10, 100):
	for den in xrange(num + 1, 100):
		if len({d for d in str(num)+str(den)}) != 3: continue
		snum, sden = map(int, str(num)), map(int, str(den))
		if not (snum[0] == sden[1] or snum[1] == sden[0]): continue
		if 0 in snum or 0 in sden: continue
		fraction = num / float(den)
		f = snum[0] / float(sden[1])
		if fraction == f: result.append(f)
		f = snum[1] / float(sden[0])
		if fraction == f: result.append(snum[1] / float(sden[0]))

print reduce(lambda x,y: x*y, result)