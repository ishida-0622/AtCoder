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
# 真 if 式 else 偽 <- 三項演算子
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート

def In():return input().rstrip()
def intIn():return int(input().rstrip())
def mapStr():return map(str, input().rstrip().split())
def mapInt():return map(int, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def splitStr():return input().rstrip().split()
def listStr():return list(input().rstrip())
def YesNo(flag:bool, yes="Yes", no="No"):print(yes) if flag else print(no)
def yesno(flag:bool, yes="yes", no="no"):print(yes) if flag else print(no)
def YESNO(flag:bool, yes="YES", no="NO"):print(yes) if flag else print(no)




n = intIn()
sm = 0
i = 0
while sm < n:
    i += 1
    sm += i
print(i)