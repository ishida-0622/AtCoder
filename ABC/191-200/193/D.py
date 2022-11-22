import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque, defaultdict
from itertools import combinations, permutations, accumulate
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
max___ = max
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



k = int(input())
s = input()
t = input()

cards = [k-((s[:-1]+t[:-1]).count(str(i))) for i in range(1,10)]

s_point = sum([i * 10 ** s[:-1].count(str(i)) for i in range(1, 10)])
t_point = sum([i * 10 ** t[:-1].count(str(i)) for i in range(1, 10)])

cnt = 0

for i in range(1, 10):
    for j in range(1, 10):
        takahashi = sum([ii * 10 ** (s[:-1]+str(i)).count(str(ii)) for ii in range(1, 10)])
        aoki = sum([ii * 10 ** (t[:-1]+str(j)).count(str(ii)) for ii in range(1, 10)])
        if takahashi > aoki:
            if i == j:
                cnt += cards[i-1] * (cards[j-1]-1)
            else:
                cnt += cards[i-1] * cards[j-1]

print(cnt / ((k*9-8) * (k*9-9)))
