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

def In():return input().rstrip()
def intIn():return int(input().rstrip())
def mapInt():return map(int, input().rstrip().split())
def mapStr():return map(str, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def listMapStr():return list(map(str, input().rstrip().split()))
def yesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)



h,w = mapInt()
lst = [list(In()) for _ in range(h)]


def re(a=None,b=None,c=None,d=None):
    num = ["1", "2", "3", "4", "5", None, None, None, None, ".", ".", ".", "."]
    l = [a,b,c,d]
    for i in l:
        if i in num:
            num.remove(i)
    return num[0]

if h > 1 and w > 1:
    for i, ls in enumerate(lst):
        for j, s in enumerate(ls):
            if s == ".":
                if i == 0:
                    if j == 0:
                        ls[j] = re(ls[j+1], lst[i+1][j])
                    elif j == w-1:
                        ls[j] = re(ls[j-1], lst[i+1][j])
                    else:
                        ls[j] = re(ls[j-1], ls[j+1], lst[i+1][j])
                elif i == h-1:
                    if j == 0:
                        ls[j] = re(ls[j+1], lst[i-1][j])
                    elif j == w-1:
                        ls[j] = re(ls[j-1], lst[i-1][j])
                    else:
                        ls[j] = re(ls[j-1], ls[j+1], lst[i-1][j])
                elif j == 0:
                    ls[j] = re(ls[j+1], lst[i+1][j], lst[i-1][j])
                elif j == w-1:
                    ls[j] = re(ls[j-1], lst[i+1][j], lst[i-1][j])
                else:
                    ls[j] = re(ls[j+1], ls[j-1], lst[i+1][j], lst[i-1][j])
else:
    if h == 1 and w == 1:
        if lst[0][0] == ".":
            lst[0][0] = "1"
    elif h == 1:
        for i in range(w):
            if lst[0][i] == ".":
                if i == 0:
                    lst[0][i] = re(lst[0][i+1])
                elif i == w-1:
                    lst[0][i] = re(lst[0][i-1])
                else:
                    lst[0][i] = re(lst[0][i+1], lst[0][i-1])
    else:
        for i in range(h):
            if lst[i][0] == ".":
                if i == 0:
                    lst[i][0] = re(lst[i+1][0])
                elif i == h-1:
                    lst[i][0] = re(lst[i-1][0])
                else:
                    lst[i][0] = re(lst[i+1][0], lst[i-1][0])


for i in lst:
    print(*i, sep="")