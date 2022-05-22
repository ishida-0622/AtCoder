# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.deepcopy()
from collections import deque
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def intIn():return int(input())
def mapInt():return map(int, input().rstrip().split())
def mapStr():return map(str, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def listMapStr():return list(map(str, input().rstrip().split()))
def yesNo(flag,yes="Yes",no="No"):print(yes) if flag else print(no)



X = [1,0]
Y = [0,1]
def bfs(start):
    global lst
    pos = deque(start)
    while len(pos) > 0:
        x,y,cnt = pos.popleft()
        for i in range(2):
            nx = x + X[i]
            ny = y + Y[i]
            if nx < h and ny < w and lst[nx][ny] == ".":
                lst[nx][ny] = "#"
                pos.append((nx,ny,cnt+1))
    return cnt



h,w = mapInt()
lst = [list(input().rstrip()) for _ in range(h)]
st = deque([(0,0,1)])
print(bfs(st))