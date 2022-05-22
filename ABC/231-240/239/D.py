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
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]



a, b, c, d = map(int, inputSys().rstrip().split())
ans = "Aoki"
for i in range(a,b+1):
    flg = False
    for j in range(c,d+1):
        if j+i in prime:
            flg = True
    if not flg:
        ans = "Takahashi"
print(ans)
