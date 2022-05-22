# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.copy copy.deepcopy
import sys
# input = sys.stdin.readline # rstrip()
sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))


def dfs(pos, seki):
    global n
    if pos == n:
        if seki == x:
            global ans
            ans += 1
        return
    for i in lst[pos]:
        if seki > x // i:
            continue
        dfs(pos+1,seki*i)

ans = 0
n,x = mapInt()
lst = [list(map(int, input().split()[1:])) for _ in range(n)]
dfs(0,1)
print(ans)