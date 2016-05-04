import sys
import matplotlib.pyplot as plt
import numpy as np
from math import log

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
options = []
smaller_games = []
smaller_games_opts = []
smaller_games.append("P")
smaller_games_opts.append(0)

for i in xrange(1, n-1):
    options = list(set(get_opts(primes(i+1))))
    smaller_games.append("P")
    smaller_games_opts.append(len(options))
    for o in options:
        if smaller_games[i-o] is "P":
            smaller_games[i] = "N"
            break

p_str = ""
lower = 0 if len(sys.argv) < 4 else int(sys.argv[3])
thresh = 2 if len(sys.argv) < 3 else int(sys.argv[2])
o_count = [0,0,0,0,0,0,0,0,0,0,0,0]
n_o_count = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in xrange(lower, n-1):
    o_count[smaller_games_opts[i]] = o_count[smaller_games_opts[i]] + 1
    if smaller_games[i] is "N":
        n_o_count[smaller_games_opts[i]] = n_o_count[smaller_games_opts[i]] + 1

print o_count
print n_o_count
