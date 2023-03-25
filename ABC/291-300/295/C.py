from collections import Counter

n = int(input())
lst = list(map(int, input().split()))
cnt = Counter(lst)
print(sum(v // 2 for v in cnt.values()))
