import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n, Q = map(int, inputSys().split())
v = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, inputSys().split())
    v[a].append(b)
    v[b].append(a)

V = [None] * (n+1)

def dfs(c, m):
    for val in v[c]:
        if V[val] == None:
            V[val] = m % 2
            dfs(val, m+1)

dfs(1,0)

for _ in range(Q):
    c, d = map(int, inputSys().split())
    if V[c] == V[d]:
        print("Town")
    else:
        print("Road")
