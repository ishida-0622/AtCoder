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



def main():
    n, m = map(int, input().split())
    is_seen = [False] * n
    node = [[] for _ in range(n)]
    lst = [None] * n
    for _ in range(m):
        l, r, d = map(int, input().split())
        l, r = l-1, r-1
        node[l].append((r, d, "R"))
        node[r].append((l, d, "L"))

    for i in range(n):
        if is_seen[i]:
            continue
        is_seen[i] = True
        lst[i] = 0
        que = deque([i])
        while que:
            now = que.popleft()
            for a, d, s in node[now]:
                if lst[a] == None:
                    lst[a] = lst[now] + (d if s == "R" else -d)
                    is_seen[a] = True
                    que.append(a)
                else:
                    if lst[a] != lst[now] + (d if s == "R" else -d):
                        no()
    yes()

if __name__ == "__main__":
    main()
