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

def mex(s):
    if not '0' in s:
        return '0'
    elif not '*' in s:
        return '*'
    i = 2
    while '*' + str(i) in s:
        i = i + 1
    return '*' + str(i)

n = 10 if len(sys.argv) < 2 else int(sys.argv[1])
options = []
smaller_games = []
smaller_games_opts = []
smaller_games.append("P")
smaller_games_opts.append(0)

#game_sets = [set([])]
game_type = ['0']

for i in xrange(1, n-1):
    options = list(set(get_opts(primes(i+1))))
    smaller_games.append("P")
    smaller_games_opts.append(len(options))
    subgames = []
    for o in options:
        if smaller_games[i-o] is "P":
            smaller_games[i] = "N"
        subgames.append(game_type[i-o])
    #game_sets.append(set(subgames))
    game_type.append(mex(set(subgames)))

'''
    if set(subgames) == set(['0']) or set(subgames) == set(['0', '*2']):
        game_type.append('*')
    elif set(subgames) == set(['0', '*']):
        game_type.append('*2')
    elif set(subgames) == set(['0', '*', '*2']):
        game_type.append('*3')
    elif '*' in subgames or '*2' in subgames or 'alpha' in subgames or 'beta' in subgames:
        game_type.append('0')
    else:
        print subgames
        game_type.append('other')
'''
#print game_sets
#print game_type

otot = 0
star_tot = 0
star_2_tot = 0
star_3_tot = 0
star_4_tot = 0
other_tot = 0
for i in xrange(0, n-1):
    if game_type[i] is '0':
        otot = otot + 1
    if game_type[i] is '*':
        star_tot = star_tot + 1
    if '*2' in game_type[i]:
        star_2_tot = star_2_tot + 1
    if '*3' in game_type[i]:
        star_3_tot = star_3_tot + 1
    if '*4' in game_type[i]:
        star_4_tot = star_4_tot + 1
    if game_type[i] is 'other':
        other_tot = other_tot + 1

print '0:  ', otot
print '*:  ', star_tot
print '*2: ', star_2_tot
print '*3: ', star_3_tot
print '*4: ', star_4_tot
print 'other: ', other_tot

'''
p_str = ""
lower = 0 if len(sys.argv) < 4 else int(sys.argv[3])
thresh = 2 if len(sys.argv) < 3 else int(sys.argv[2])
o_count = [0,0,0,0,0,0,0,0,0,0,0,0]
n_o_count = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in xrange(lower, n-1):
    o_count[smaller_games_opts[i]] = o_count[smaller_games_opts[i]] + 1
    if "*" in smaller_games[i]:
        n_o_count[smaller_games_opts[i]] = n_o_count[smaller_games_opts[i]] + 1

print o_count
print n_o_count
'''
