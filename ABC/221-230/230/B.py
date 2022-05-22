import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

s = input().replace("\n","")
t = "oxx" * 100

if s in t:
    print("Yes")
else:
    print("No")
