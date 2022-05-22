# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def intIn():return int(input())
def mapInt():return map(int, input().rstrip().split())
def mapStr():return map(str, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def listMapStr():return list(map(str, input().rstrip().split()))
def yesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)



lst = ["ABC","ARC","AGC","AHC"]
lst2 = [input().rstrip() for _ in range(3)]
for i in lst2:
    lst.remove(i)
print(lst[0])