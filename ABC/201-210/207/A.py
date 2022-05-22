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
inf = float("inf")
minf = -float("inf")
# prime = [
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
# 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
# 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
# 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
# 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
# 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
# 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
# 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
# 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
# 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
# ]
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



ls = listMapInt()
ls.remove(min(ls))
print(sum(ls))
