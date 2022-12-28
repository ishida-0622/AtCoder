n = int(input())
print(*sum([list(val) for val in zip(*input().split())], []), sep="")
