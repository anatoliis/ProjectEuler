#!/usr/bin/env python2
import itertools

result = 0
for n in itertools.permutations('9876543210'):
	n = ''.join(n)
	if not int(n[0]): continue
	if int(n[1:4]) % 2: continue
	if int(n[2:5]) % 3: continue
	if int(n[3:6]) % 5: continue
	if int(n[4:7]) % 7: continue
	if int(n[5:8]) % 11: continue
	if int(n[6:9]) % 13: continue
	if int(n[7:10]) % 17: continue
	result += int(n)

print 'result: %s' % result