#!/usr/bin/env pypy

target = 200
coin_set = [1, 2, 5, 10, 20, 50, 100, 200]

ways = [1] + [0] * target
print len(ways)
for coin in coin_set:
	for i in xrange(coin, target + 1):
		ways[i] += ways[i - coin]

print 'result: %s' % ways[-1]