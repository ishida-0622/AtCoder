# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰
# 条件式が真のときに返す値 if 条件式 else 条件式が偽のときに返す値 <- 三項演算子

def intIn():return int(input())
def strIn():return input().rstrip()
def mapInt():return map(int, input().rstrip().split())
def mapStr():return map(str, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def listMapStr():return list(map(str, input().rstrip().split()))
def yesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)



s = list(input().rstrip())
lst = [int(s[0]+s[1]+s[2]), int(s[1]+s[2]+s[0]), int(s[2]+s[0]+s[1])]
print(sum(lst))