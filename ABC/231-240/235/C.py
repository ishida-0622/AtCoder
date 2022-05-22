import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**6)
import copy  # copy.deepcopy()
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float('inf')
minf = -float('inf')
def YesNo(flag: bool, yes='Yes', no='No'): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n,q = map(int, inputSys().rstrip().split())
a = list(map(int, inputSys().rstrip().split()))
dic = {}
for i, val in enumerate(a):
    if dic.get(val) == None:
        dic[val] = [i+1]
    else:
        dic[val].append(i+1)

for i in range(q):
    x,k = map(int, inputSys().rstrip().split())
    if dic.get(x) != None and len(dic[x]) >= k:
        print(dic[x][k-1])
    else:
        print(-1)
