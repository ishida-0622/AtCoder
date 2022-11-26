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



def calc(a, g):
    return a / math.sqrt(g)

def f(n):
    return A / math.sqrt(1+n) + n * B

A, B = map(int, input().split())
ans = calc(A, 1)

N = A

ll, l, r, rr = 0, N//4*2, N//4*3, N
while ll < rr and rr-ll > 3:
    # tmp_ll = calc(A, max(1, ll)) + (max(0, ll-1) * B)
    tmp_ll = f(ll)
    # tmp_l = calc(A, max(1,l)) + (max(0,l-1) * B)
    tmp_l = f(l)
    # tmp_r = calc(A, max(1,r)) + (max(0,r-1) * B)
    tmp_r = f(r)
    # tmp_rr = calc(A, max(1,rr)) + (max(0,rr-1) * B)
    tmp_rr = f(rr)
    ls = sorted([tmp_ll, tmp_l, tmp_r, tmp_rr])
    if ls[0] == tmp_ll:
        rr = l
        r = ll + (rr-ll) // 4 * 3
        l = ll + (rr-ll) // 4 * 2
    elif ls[0] == tmp_rr:
        ll = r
        r = ll + (rr-ll) // 4 * 3
        l = ll + (rr-ll) // 4 * 2
    elif ls[0] == tmp_l:
        rr = r
        r = ll + (rr-ll) // 4 * 3
        l = ll + (rr-ll) // 4 * 2
    else:
        ll = l
        r = ll + (rr-ll) // 4 * 3
        l = ll + (rr-ll) // 4 * 2
    ans = min([ans, tmp_ll, tmp_l, tmp_r, tmp_rr])
print(f"{ans:.7f}")
