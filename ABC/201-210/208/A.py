import itertools # 順列全探索(nCr) permutations()
import bisect # 二分探索
import math
import string
a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
a_Z = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
n0_9 = string.digits # 0123456789
import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
sys.setrecursionlimit(10**6) # 再帰
# 条件式が真のときに返す値 if 条件式 else 条件式が偽のときに返す値 <- 三項演算子

def In():return input().rstrip()
def intIn():return int(input().rstrip())
def mapStr():return map(str, input().rstrip().split())
def mapInt():return map(int, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def splitStr():return input().rstrip().split()
def listStr():return list(input().rstrip())
def YesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)
def yesno(flag, yes="yes", no="no"):print(yes) if flag else print(no)
def YESNO(flag, yes="YES", no="NO"):print(yes) if flag else print(no)




a,b = mapInt()
YesNo(a*6 >= b and a <= b)