a,b,k = map(int, input().split())
if a < k:
    b -= k-a
a -= k
if a < 0:
    a = 0
if b < 0:
    b = 0
print(a,b)