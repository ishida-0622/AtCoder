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



L, N1, N2 = map(int, input().split())
ans = 0
A = [tuple(map(int, input().split())) for _ in range(N1)]
B = [tuple(map(int, input().split())) for _ in range(N2)]

i, j = 0, 0
cnt_a, cnt_b = 0, 0
while len(A) > i and len(B) > j:
    if A[i][1] - cnt_a == B[j][1] - cnt_b:
        ans += A[i][1] - cnt_a if A[i][0] == B[j][0] else 0
        cnt_a, cnt_b = 0, 0
        i += 1
        j += 1
    elif A[i][1] - cnt_a > B[j][1] - cnt_b:
        ans += B[j][1] - cnt_b if A[i][0] == B[j][0] else 0
        cnt_a += B[j][1] - cnt_b
        j += 1
        cnt_b = 0
    else:
        ans += A[i][1] - cnt_a if A[i][0] == B[j][0] else 0
        cnt_b += A[i][1] - cnt_a
        i += 1
        cnt_a = 0
print(ans)
