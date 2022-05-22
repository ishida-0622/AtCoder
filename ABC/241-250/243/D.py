n, x = map(int, input().split())
s = input()
stack = []
for i in range(n):
    if stack == []:
        stack.append(s[i])
    else:
        if s[i] == "U":
            if stack[-1] == "R" or stack[-1] == "L":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

for i in stack:
    if i == "R":
        x *= 2
        x += 1
    elif i == "L":
        x *= 2
    else:
        x //= 2
print(x)
