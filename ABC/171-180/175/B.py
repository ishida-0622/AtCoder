n = int(input())
lst = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = sorted([lst[i], lst[j], lst[k]])
            if a != b and a != c and b != c and a+b > c:
                ans += 1
print(ans)
