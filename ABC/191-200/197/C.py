import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



def calc_or(arr):
    res = 0
    for v in arr:
        res |= v
    return res

def calc_xor(arr):
    res = 0
    for v in arr:
        res ^= v
    return res

def f(select):
    if len(select) == 0:
        return inf
    _or = []
    for i in range(len(select)):
        if i == 0:
            _or.append(calc_or(lst[:select[i]]))
        else:
            _or.append(calc_or(lst[select[i-1]:select[i]]))

        if i == len(select)-1:
            _or.append(calc_or(lst[select[i]:]))
    return calc_xor(_or)


n = int(input())
lst = list(map(int, input().split()))
ans = calc_or(lst)

for i in range(2 ** (n-1)):
    selected = []
    for j in range(n):
        if (i >> j) & 1:
            selected.append(j+1)
    ans = min(ans, f(selected))

print(ans)
