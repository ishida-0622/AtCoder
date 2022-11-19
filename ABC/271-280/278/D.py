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
lst = list(map(int, input().split()))
Q = int(input())
dic = defaultdict(int)
all = -1

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        all = query[1]
        dic = defaultdict(int)
    elif query[0] == 2:
        dic[query[1]-1] += query[2]
    else:
        if all < 0:
            print(lst[query[1]-1] + dic[query[1]-1])
        else:
            print(all + dic[query[1]-1])
