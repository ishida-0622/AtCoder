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



def L(now, l):
    i, j = now
    if i in dic_i:
        idx = bisect.bisect_right(dic_i[i], j)
        if idx >= len(dic_i[i]):
            return max(dic_i[i][-1]+1, j-l)
        a = dic_i[i][max(idx-1, 0)]
        if a > j:
            return max(1, j-l)
        else:
            return max(a+1, j-l)
    else:
        return max(1, j-l)

def R(now, l):
    i, j = now
    if i in dic_i:
        idx = bisect.bisect_left(dic_i[i], j)
        if idx >= len(dic_i[i]):
            return min(W, j+l)
        a = dic_i[i][min(idx, len(dic_i[i])-1)]
        if a < j:
            return min(W, j+l)
        else:
            return min(a-1, j+l)
    else:
        return min(W, j+l)

def U(now, l):
    i, j = now
    if j in dic_j:
        idx = bisect.bisect_right(dic_j[j], i)
        if idx >= len(dic_j[j]):
            return max(dic_j[j][-1]+1, i-l)
        a = dic_j[j][max(idx-1, 0)]
        if a > i:
            return max(1, i-l)
        else:
            return max(a+1, i-l)
    else:
        return max(1, i-l)

def D(now, l):
    i, j = now
    if j in dic_j:
        idx = bisect.bisect_left(dic_j[j], i)
        if idx >= len(dic_j[j]):
            return min(H, i+l)
        a = dic_j[j][min(idx, len(dic_j[j])-1)]
        if a < i:
            return min(H, i+l)
        else:
            return min(a-1, i+l)
    else:
        return min(H, i+l)


H, W, rs, cs = map(int, inputSys().split())
n = int(inputSys())
wall = [list(map(int, inputSys().split())) for _ in range(n)]
Q = int(inputSys())

now = [rs, cs]
dic_i = {}
dic_j = {}
for val in wall:
    i, j = val
    if i in dic_i:
        bisect.insort(dic_i[i], j)
    else:
        dic_i[i] = [j]
    if j in dic_j:
        bisect.insort(dic_j[j], i)
    else:
        dic_j[j] = [i]

for i in range(Q):
    d, l = inputSys().split()
    l = int(l)
    if d == "L":
        a = L(now, l)
        now[1] = a
        print(*now)
    if d == "R":
        a = R(now, l)
        now[1] = a
        print(*now)
    if d == "U":
        a = U(now, l)
        now[0] = a
        print(*now)
    if d == "D":
        a = D(now, l)
        now[0] = a
        print(*now)
