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



a, b, c, d = map(int, input())
for i in range(2):
    ab = a+b if i % 2 else a-b
    for j in range(2):
        abc = ab+c if j % 2 else ab-c
        for k in range(2):
            if (abc+d if k % 2 else abc-d) == 7:
                op1 = "+" if i % 2 else "-"
                op2 = "+" if j % 2 else "-"
                op3 = "+" if k % 2 else "-"
                print(f"{a}{op1}{b}{op2}{c}{op3}{d}=7")
                exit()
