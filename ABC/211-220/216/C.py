import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ans = []

while n > 0:
    if n % 2 == 0:
        ans.append("B")
        n //= 2
    else:
        ans.append("A")
        n -= 1
ans.reverse()
print(*ans, sep="")