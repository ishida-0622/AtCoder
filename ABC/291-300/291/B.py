n = int(input())
print(sum(sorted(list(map(int, input().split())))[n:n*4]) / (3*n))
