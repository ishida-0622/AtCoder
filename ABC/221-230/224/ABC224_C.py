# x1y2 + x2y3 + x3y1 - y1x2 - y2x3 - y3x1
n = int(input())
ncr = int((n * (n - 1) * (n - 2)) / 6) # n個の点から3個選ぶ組み合わせ
cnt = 0

lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if ((lst[i][0] * lst[j][1]) + (lst[j][0] * lst[k][1]) + (lst[k][0] * lst[i][1]) - (lst[i][1] * lst[j][0]) - (lst[j][1] * lst[k][0]) - (lst[k][1] * lst[i][0])) == 0:
                cnt += 1

print(ncr - cnt)