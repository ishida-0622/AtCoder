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



n, x, y = map(int, inputSys().split())
V = [[] for _ in range(n+1)]
node = [[False, -1, -1] for _ in range(n+1)]
node[x] = [True, 0, 0]

for i in range(n-1):
    u, v = map(int, inputSys().split())
    V[u].append(v)
    V[v].append(u)


que = deque([x])
while len(que) > 0:
    a = que.popleft()
    if a == y:
        break
    for val in V[a]:
        if not node[val][0]:
            node[val] = [True, a, node[a][2]+1]
            que.append(val)

ans = [y]
tmp = node[y][1]
for _ in range(node[y][2]):
    ans.append(tmp)
    tmp = node[tmp][1]

print(*reversed(ans))
