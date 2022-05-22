h, w = map(int, input().split())
c = [list(map(int,input().split())) for _ in range(h)]
flag = True

for i in range(h):
    for j in range(w):
        for a in range(1, h - i):
            for b in range(1, w - j):
                if c[i][j] + c[i+a][j+b] > c[i+a][j] + c[i][j+b]:
                    flag = False
                    break

if flag:
    print('Yes')
else:
    print('No')