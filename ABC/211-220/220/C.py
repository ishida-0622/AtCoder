# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

n = int(input())
lst = listMapInt()
sumNum = sum(lst)
x = int(input())
cnt = x // sumNum * n
m = cnt // n * sumNum
while m <= x:
    m += lst[cnt % n]
    cnt += 1
print(cnt)