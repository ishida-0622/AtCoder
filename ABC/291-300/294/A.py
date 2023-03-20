n = int(input())
print(*filter(lambda x: not x % 2, map(int, input().split())))
