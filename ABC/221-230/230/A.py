import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n = int(input())
if n >= 42:
    n += 1

n = str(n)

print("AGC{}".format(n.zfill(3)))
