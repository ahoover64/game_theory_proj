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
smaller_games.append("P")

for i in xrange(1, n-1):
    options = get_opts(primes(i+1))
    smaller_games.append("P")
    for o in options:
        if smaller_games[i-o] is "P":
            smaller_games[i] = "N"
            break

p_str = ""
p_tot = 0
n_tot = 0
n_data = []
p_data = []
lower = 0 if len(sys.argv) < 4 else int(sys.argv[3])
n_row = 0
p_row = 0
n_row_tot = 0
p_row_tot = 0
thresh = 2 if len(sys.argv) < 3 else int(sys.argv[2])
for i in xrange(lower, n-1):
    if smaller_games[i] is "P":
        p_tot = p_tot + 1
        p_row = p_row + 1
        if n_row == thresh:
            n_row_tot = n_row_tot + 1
        n_row = 0
    elif smaller_games[i] is "N":
        n_tot = n_tot + 1
        n_row = n_row + 1
        if p_row == thresh:
            p_row_tot = p_row_tot + 1
        p_row = 0
    else:
        print "strange thing happened"
    if i % (n / 100) is 0:
        n_data.append((i, n_tot))
        p_data.append((i, p_tot))


print "N Total: ", n_tot
print "P Total: ", p_tot
print "N Row Total: ", n_row_tot
print "P Row Total: ", p_row_tot

n_zipped = zip(n_data)
p_zipped = zip(p_data)
n_x = []
n_y = []
p_x = []
p_y = []
for i in xrange(len(n_zipped)):
    n_x.append(n_zipped[i][0][0])
    n_y.append(n_zipped[i][0][1])
    p_x.append(p_zipped[i][0][0])
    p_y.append(p_zipped[i][0][1])

n_par = np.polyfit(n_x, n_y, 1, full=True)
p_par = np.polyfit(p_x, p_y, 1, full=True)
print "N = " + str(n_par[0][0]) + " * n + " + str(n_par[0][1])
print "P = " + str(p_par[0][0]) + " * n + " + str(p_par[0][1])

n_plot = plt.scatter(*zip(*n_data), color='red')
p_plot = plt.scatter(*zip(*p_data), color='blue')


#plt.plot([0, n], [0, n_tot], 'k-', lw=2)
#plt.plot([0, n], [0, p_tot], 'k-', lw=2)
plt.xlabel('n')
axes = plt.gca()
axes.set_xlim([0,n*1.05])
axes.set_ylim([0,max(n_tot, p_tot) * 1.05])
plt.legend((n_plot, p_plot),
           ('Total number of N states < n', 'Total number of P states < n'),
           scatterpoints=1,
           loc='upper left')
plt.show()

#print p_str
