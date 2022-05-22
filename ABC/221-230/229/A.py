import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

list = [input() for _ in range(2)]

if list[0][0] == list[1][1] and list[0][1] == list[1][0] and list[0][0] != list[0][1]:
    print("No")
else:
    print("Yes")