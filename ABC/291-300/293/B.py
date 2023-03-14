n = int(input())
lst = list(map(int, input().split()))
is_call = [False] * n

for i, v in enumerate(lst):
    if is_call[i]:
        continue
    is_call[v-1] = True

ans = [i+1 for i, v in enumerate(is_call) if not v]
print(len(ans))
print(*sorted(ans))
