#!/usr/bin/env python2

def triangle(number):
	n = ((number * 8 + 1)**0.5 - 1) / 2
	return n.is_integer()

def value(word):
	return sum(map(lambda letter: ord(letter)-64, word))

with open('p042_words.txt', 'r') as f:
	words = f.read().replace('"', '').split(',')

print 'result: %s' % sum(triangle(value(word)) for word in words)