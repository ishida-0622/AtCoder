import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt, floor, ceil, radians, sin, cos, tan, pi
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate, groupby
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
def lcm(a: int, b: int): return a*b // gcd(a,b)
def round(n: int, d: int = 0): return float(Decimal(n).quantize(Decimal(f"1e{d}"), ROUND_HALF_UP))



def main():
    n, t = map(int, input().split())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    ans = None
    t = t if t in set(C) else C[0]
    for i in range(n):
        if C[i] == t:
            if ans == None or R[i] > R[ans]:
                ans = i
    print(ans+1)

if __name__ == "__main__":
    main()
