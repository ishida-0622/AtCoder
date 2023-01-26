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
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



lst = [list(map(int, input().split())) for _ in range(3)]
ls = [[False] * 3 for _ in range(3)]
n = int(input())

for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if lst[i][j] == b:
                ls[i][j] = True

for i in range(3):
    if sum(ls[i]) == 3:
        yes()
    if ls[0][i] and ls[1][i] and ls[2][i]:
        yes()
if ls[0][0] and ls[1][1] and ls[2][2]:
    yes()
if ls[0][2] and ls[1][1] and ls[2][0]:
    yes()
no()
