import itertools # 順列全探索(nCr) permutations()
import bisect # 二分探索
import math
import string
a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
a_Z = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
zero_nine = string.digits # 0123456789
import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
sys.setrecursionlimit(10**6) # 再帰
# 真 if 式 else 偽 <- 三項演算子
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート(key -> x: x[0])

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




N,L,W = mapInt()
lst = listMapInt()
ans = 0
if lst[0] > 0:
    ans += lst[0] // W
    if lst[0] % W != 0:
        ans += 1

for i in range(N-1):
    n = lst[i]
    m = lst[i+1]
    if n + W < m:
        tmp = m - (n + W)
        ans += tmp // W
        if tmp % W != 0:
            ans += 1

if lst[-1] + W < L:
    n = L - (lst[-1] + W)
    if n % W == 0:
        ans += n // W
    else:
        ans += n // W + 1

print(ans)