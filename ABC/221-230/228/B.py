import sys
input = sys.stdin.readline

n,x = map(int, input().split())
lst = [0 for _ in range(n)]
lst2 = list(map(int, input().split()))

i = x * 1
while True:
    if lst[i-1] == 0:
        lst[i-1] = 1
        i = lst2[i-1]
    else:
        break

print(sum(lst))