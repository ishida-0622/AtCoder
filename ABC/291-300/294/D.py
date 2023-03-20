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



n, Q = map(int, input().split())
lst = list(range(n, 0, -1))
calls = set([])
_min = inf
que = deque([])

for _ in range(Q):
    event = input().split()
    if event[0] == "1":
        item = lst.pop()
        calls.add(item)
        que.append(item)
        _min = min(_min, item)
    elif event[0] == "2":
        x = int(event[1])
        calls.remove(x)
        if x == _min:
            while _min not in calls:
                if len(que) == 0:
                    _min = inf
                    break
                _min = que.popleft()
    else:
        print(_min)
