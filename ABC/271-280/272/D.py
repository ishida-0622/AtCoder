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



n, m = map(int, inputSys().split())
lst = [[-1] * n for _ in range(n)]
lst[0][0] = 0
ls = []

for i in range(n):
    for j in range(n):
        if (((i) ** 2) + ((j) ** 2)) == m:
            ls.append([i,j])


que = deque([[0, 0, 0]])

while len(que):
    x, y, cnt = que.popleft()
    for val in ls:
        a, b = val
        if x+a < n and y+b < n and lst[x+a][y+b] == -1:
            lst[x+a][y+b] = cnt+1
            que.append([x+a, y+b, cnt+1])
        if x-a >= 0 and y-b >= 0 and lst[x-a][y-b] == -1:
            lst[x-a][y-b] = cnt+1
            que.append([x-a, y-b, cnt+1])
        if x+a < n and y-b >= 0 and lst[x+a][y-b] == -1:
            lst[x+a][y-b] = cnt+1
            que.append([x+a, y-b, cnt+1])
        if x-a >= 0 and y+b < n and lst[x-a][y+b] == -1:
            lst[x-a][y+b] = cnt+1
            que.append([x-a, y+b, cnt+1])


for val in lst:
    print(*val)
