import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート


from collections import deque
def bfs(x, k):
    res = 0
    que = deque([[x, k]])
    st = {x} # 既に探索した頂点
    while len(que) > 0:
        pos, num = que.popleft()
        res += pos
        if num == 0: # 深さkなら終了
            continue
        for val in lst[pos]: # 頂点xの隣接頂点
            if val not in st: # 探索済みか
                que.append([val, num-1]) # queに追加
                st.add(val) # 探索済みとしてセット
    return res



n, m = map(int, inputSys().split())
lst = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, inputSys().split())
    lst[a].append(b)
    lst[b].append(a)

Q = int(inputSys())
for i in range(Q):
    x, k = map(int, inputSys().split())
    print(bfs(x, k))
