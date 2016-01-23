import random

cpdef sprime(int n):
	if n < 3: return n == 2
	if n & 1 == 0: return False
	cdef int i
	for i in xrange(3, int(n**0.5) + 1, 2):
		if not n % i: return False
	return True

cpdef prime(int n):
	if n < 3: return n == 2
	if not n & 1: return False
	small_primes = (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,
		71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,
		157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,
		241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,
		347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,
		439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,
		547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,
		643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,
		751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,
		859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,
		977,983,991,997)
	cdef int p
	for p in small_primes:
		if n < p * p: return True
		if n % p == 0: return False
	cdef int r, s, x, a, _
	r = 0; s = n - 1
	while not s & 1: r += 1; s /= 2
	if n < 2047: bases = (2)
	elif n < 1373653: bases = (2,3)
	elif n < 9080191: bases = (31,73)
	elif n < 25326001: bases = (2,3,5)
	elif n < 4759123141: bases = (2,7,61)
	elif n < 1122004669633: bases = (2,13,23,1662803)
	elif n < 2152302898747: bases = (2,3,5,7,11)
	elif n < 3474749660383: bases = (2,3,5,7,11,13)
	elif n < 341550071728321: bases = (2,3,5,7,11,13,17)
	elif n < 3825123056546413051: bases = (2,3,5,7,11,13,17,19,23)
	else: bases = (2,3,5,7,11,13,17,19,23,29,31,37)
	for a in bases:
		x = pow(a, s, n)
		if x == 1 or x == n - 1: continue
		for _ in xrange(r - 1):
			x = pow(x, 2, n)
			if x == n - 1: break
		else: return False
	return True

cpdef primes_list(int n):
	cdef int i
	sieve = [True] * n
	for i in xrange(3, int(n**0.5) + 1, 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
	return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

cpdef primes_half(int n):
	cdef int i
	sieve = [True] * (n/2)
	for i in xrange(3, int(n**0.5) + 1, 2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
	return [2] + [2 * i + 1 for i in xrange(1, n/2) if sieve[i]]