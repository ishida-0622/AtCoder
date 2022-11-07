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



def f(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    return x

def ff(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    while x % 3 == 0:
        x //= 3
        cnt += 1
    return cnt


n = int(input())
lst = list(map(int, input().split()))
mod_lst = list(map(f, lst))
if len(set(mod_lst)) > 1:
    print(-1)
    exit()

m = gcd(lst[0], lst[1])
for val in lst:
    m = gcd(m, val)

print(sum(map(ff, map(lambda x: x // m, lst))))
