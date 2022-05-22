import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**6)  # 再帰
import copy  # copy.deepcopy()
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗 非整数.負数はValueError, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
a_z = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
A_Z = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
a_Z = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
zero_nine = string.digits  # 0123456789
mod = 998244353
mod2 = 1000000007
def In(): return inputSys().rstrip()
def intIn(): return int(In())
def listStr(): return list(In())
def splitStr(): return In().split()
def mapInt(): return map(int, splitStr())
def listMapInt(): return list(mapInt())
def twoArrInt(h: int): return [listMapInt() for _ in range(h)]
def twoArrStrList(h: int): return [listStr() for _ in range(h)]
def twoArrStrSplit(h: int): return [splitStr() for _ in range(h)]
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def yesno(flag: bool): YesNo(flag, "yes", "no")
def YESNO(flag: bool): YesNo(flag, "YES", "NO")
def OKNG(flag: bool): YesNo(flag, "OK", "NG")
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート
# 真 if 式 else 偽 <- 三項演算子



n = intIn()
lst = listMapInt()
dp = [[0]*10 for _ in range(n+1)]
dp[0][lst[0]] = 1

for i in range(n-1): # 2*10^5
    for j in range(10): # 10
        if dp[i][j] >= 1:
            dp[i+1][(j + lst[i+1]) % 10] += dp[i][j] % mod
            dp[i+1][j * lst[i+1] % 10] += dp[i][j] % mod
for i in range(10):
    print(dp[n-1][i])
