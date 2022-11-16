n=int(input())
lst=[list(map(int,input().split())) for i in range(n)]
ans=10**18
for i in range(n):
    for j in range(n):
        if i == j:
            ans = min(ans,lst[i][0]+lst[j][1])
        else:
            ans = min(ans,max(lst[i][0],lst[j][1]))
print(ans)
