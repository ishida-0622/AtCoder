n, x = map(int, input().split())
s = input()
for v in s:
    if v == "o":
        x += 1
    elif x > 0:
        x -= 1
print(x)
