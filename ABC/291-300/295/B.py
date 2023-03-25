import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt, floor, ceil, sin, cos, tan, pi
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache, reduce
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
az = string.ascii_lowercase
AZ = string.ascii_uppercase
aZ = string.ascii_letters
zero_nine = string.digits
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



h, w = map(int, input().split())
lst = [list(input()) for _ in range(h)]
ans = [list("#" * w) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if lst[i][j] in zero_nine:
            n = int(lst[i][j])
            for k in range(h):
                for l in range(w):
                    if abs(i-k) + abs(j-l) <= n:
                        ans[k][l] = "."
        elif lst[i][j] == ".":
            ans[i][j] = "."

for v in ans:
    print(*v, sep="")
