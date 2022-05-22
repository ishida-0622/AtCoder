import sys
input = sys.stdin.readline  # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6)  # 再帰
import copy  # copy.deepcopy()
import itertools  # 順列全探索(nCr) permutations()
import bisect  # 二分探索
import math
import string
a_z = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
A_Z = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
a_Z = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
zero_nine = string.digits  # 0123456789
# 真 if 式 else 偽 <- 三項演算子
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート


def In(): return input().rstrip()
def intIn(): return int(input().rstrip())
def mapStr(): return map(str, input().rstrip().split())
def mapInt(): return map(int, input().rstrip().split())
def listMapInt(): return list(map(int, input().rstrip().split()))
def splitStr(): return input().rstrip().split()
def listStr(): return list(input().rstrip())
def twoArrInt(h: int): return [list(map(int, input().rstrip().split())) for _ in range(h)]
def twoArrStr(h: int): return [list(input().rstrip().split()) for _ in range(h)]
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def yesno(flag: bool, yes="yes", no="no"): print(yes) if flag else print(no)
def YESNO(flag: bool, yes="YES", no="NO"): print(yes) if flag else print(no)
def OKNG(flag: bool, ok="OK", ng="NG"): print(ok) if flag else print(ng)




n = intIn()
m = 2 ** 31
mm = -m
YesNo(mm <= n < m)