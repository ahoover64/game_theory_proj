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
options = []
smaller_games = []
smaller_games.append("P")

for i in xrange(1, n-1):
    options = get_opts(primes(i+1))
    smaller_games.append("P")
    for o in options:
        if smaller_games[i-o] is "P":
            smaller_games[i] = "N"
            break

p_tot = 0
n_tot = 0
lower = 0 if len(sys.argv) < 4 else int(sys.argv[3])
thresh = 2 if len(sys.argv) < 3 else int(sys.argv[2])
for i in xrange(lower, n-1):
    if smaller_games[i] is "P":
        p_tot = p_tot + 1
    elif smaller_games[i] is "N":
        n_tot = n_tot + 1


print "N Total: ", n_tot
print "P Total: ", p_tot
print "N_freq: ", float(n_tot) / (n-1)
print "P_freq: ", float(p_tot) / (n-1)
