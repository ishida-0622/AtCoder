import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n = int(inputSys())
lst = [inputSys().rstrip() for _ in range(n)]

def f(x, y, dx, dy):
    cnt = 0
    for i in range(6):
        if x+(dx*i) < 0 or x+(dx*i) >= n or y+(dy*i) < 0 or y+(dy*i) >= n:
            return False
        if lst[x+(dx*i)][y+(dy*i)] == "#":
            cnt += 1
    return cnt >= 4

arr = [[1,-1], [1,0], [1,1], [-1,1], [0,1], [1,1], [-1,0], [0,-1]]

for i in range(n):
    for j in range(n):
        for val in arr:
            dx, dy = val
            if f(i, j, dx, dy):
                print("Yes")
                exit()
print("No")
