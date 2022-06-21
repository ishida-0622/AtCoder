def f(x):
    re = "".join(reversed(x))
    x = "".join(reversed(re))
    return min(int(re), int(x))

n, k = map(int, input().split())
if k != f(str(k)):
    print(0)
    exit()
m = int("".join(reversed(str(k))))
kk = str(k)
mm = str(m)
ans = 0
if k != m:
    while True:
        if k <= n:
            ans += 1
            k *= 10
        elif m <= n:
            ans += 1
            m *= 10
        else:
            break
else:
    while True:
        if k <= n:
            ans += 1
            k *= 10
        else:
            break
print(ans)
