n=int(input())
lst=list(map(int,input().split()))
ans=0
_max=0
for i in range(2,998):
    tmp=0
    for j in range(n):
        if not lst[j] % i:
            tmp+=1
    if _max < tmp:
        _max=tmp
        ans=i
print(ans)
