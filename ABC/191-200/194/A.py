a,b=map(int,input().split())
ans=4
if a+b>14 and b>7:
    ans=1
elif a+b>9 and b>2:
    ans=2
elif a+b>2:
    ans=3
print(ans)
