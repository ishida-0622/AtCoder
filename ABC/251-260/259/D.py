import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect
import math
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート


def bfs(start):
    que = deque([start])
    while len(que) > 0:
        now = que.popleft()
        if now == n+1: # ゴールならYesを出力し終了
            print("Yes")
            exit()
        for val in E[now]: # 接している円
            if not V[val]: # 未到達か
                V[val] = True # 到達済みにする
                que.append(val)



n = int(inputSys())
sx, sy, tx, ty = map(int, inputSys().split())
lst = [list(map(int, inputSys().split())) for _ in range(n)]
lst.append([sx, sy, 0]) # スタート地点 半径0の円として考える
lst.append([tx, ty, 0]) # ゴール地点
E = [[] for _ in range(n+2)] # スタート地点とゴール地点が追加されているので+2

for i in range(n+1):
    x, y, r = lst[i]
    for j in range(i+1,n+2):
        xx, yy, rr = lst[j]
        d = (x-xx) ** 2 + (y-yy) ** 2 # √を使うと小数点以下の誤差が出るので次のifで半径の方を2乗
        if (r + rr) ** 2 >= d and d >= abs(r-rr) ** 2: # 接しているか？
            E[i].append(j) # 接していたら無向辺を張る
            E[j].append(i)

V = [False] * (n+2) # 全ての円を未探索として初期化
V[n] = True # スタート地点は探索済み
bfs(n) # 幅優先探索
print("No")
