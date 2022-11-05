n,a,b=map(int,input().split())
lst=list(map(int,input().split()))
ans=0
for i in range(1,n):
    ans+=min((lst[i]-lst[i-1])*a,b)
print(ans)
