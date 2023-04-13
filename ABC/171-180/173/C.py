import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt, floor, ceil, sin, cos, tan, pi
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



def black_count(arr):
    return sum(sum(arr, []))

def main():
    h, w, K = map(int, input().split())
    ans = 0
    lst = [list(map(lambda x: 0 if x == "." else 1, list(input()))) for _ in range(h)]
    for i in range(2**h):
        for j in range(2**w):
            arr = deepcopy(lst)
            for k in range(h):
                if i >> k & 1:
                    arr[k] = [0] * w
            for k in range(w):
                if j >> k & 1:
                    for l in range(h):
                        arr[l][k] = 0
            if black_count(arr) == K:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
