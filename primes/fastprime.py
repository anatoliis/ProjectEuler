def primegen():
    '''A fast sieve of Eratosthenes '''
    yield 2; yield 3; yield 5; yield 7   # original code David Eppstein, 
    sieve = {}                           #            ActiveState Recipe 2002
    ps = primegen()                      # a separate Primes Supply:
    p = next(ps) and next(ps)            # (3) a Prime to add to dict
    q = 9; c = 9                      # p * p | # (9) when its sQuare is # the next Candidate
    while True:
        if c not in sieve:            # not a multiple of any prime seen so far:
            if c < q:                 #   a prime, 
                yield c; c += 2       #
                continue              #            or
            else:   # (c==q):         #   the next prime's square:
                s = 2 * p             #     (9+6,6 : 15,21,27,33,...)
                p = next(ps)          #     (5)
                q = p * p             #     (25)
        else:                         # 'c' is a composite:
            s = sieve.pop(c)          #   step of increment
        c2 = c + s                      #   next multiple, same step
        while c2 in sieve: c2 += s    #   no multiple keys in sieve (dict):
        sieve[c2] = s                 #         (increment by the given step)
        c += 2

gen = primegen()

for i in xrange(10):
    print next(gen)