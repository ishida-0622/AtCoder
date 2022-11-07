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



n = int(input())
P = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if P[i] < P[i-1]:
        l = P[:i-1]
        r = P[i:]
        a = max___(filter(lambda x: x < P[i-1], r))
        r = sorted(list(map(lambda x: x if x != a else P[i-1], r)), reverse=True)
        print(*(l + [a] + r))
        break
