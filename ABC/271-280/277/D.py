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



n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
_sum = sum(lst)
ans = _sum

i = 0
while i < n*2:
    tmp = lst[i%n]
    j = 0
    while i+j < n*2 and (lst[(i+j)%n] == lst[(i+j+1)%n] or (lst[(i+j)%n]+1)%m == lst[(i+j+1)%n]):
        tmp += lst[(i+j+1)%n]
        j += 1
    ans = ___min(ans, max___(0, _sum - tmp))
    if j == 0:
        i += 1
    i += j

print(ans)
