import itertools # 順列全探索(nCr) permutations() <- 順列 combinations() <- 組み合わせ
# import bisect # 二分探索
import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
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



n = intIn()
lst = [listMapInt() for _ in range(n)]
Max = 0
lst2 = itertools.combinations(lst,2)

for i in lst2:
    Max = max(Max,math.sqrt(pow(i[0][0] - i[1][0], 2) + pow(i[0][1] - i[1][1],2)))
print(Max)