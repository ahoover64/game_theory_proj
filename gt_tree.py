import sys

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def get_opts(factors):
    options = []
    while factors:
        e = factors[0]
        options.append(factors.count(e))
        factors = filter(lambda a: a != e, factors)
    return options

n = 10 if len(sys.argv) < 2 else int(sys.argv[1])

store = {}
def make_store(c):
    if c is 1:
        return
    else:
        opts = []
        for i in get_opts(primes(c)):
            opts.append(c-i)
        store[c] = list(set(opts))
        for o in store[c]:
            make_store(o)

def traverse_store(c):
    if c is 1:
        print 1
        return
    print c, store[c]
    for o in sorted(store[c]):
        traverse_store(o)

make_store(n)
traverse_store(n)


