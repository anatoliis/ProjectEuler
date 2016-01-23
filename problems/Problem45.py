#!/usr/bin/env pypy

n = 144
while ((n*24*(n*2-1)+1)**0.5+1)%6: n += 1
print 'result: %s' % (2*n**2-n)