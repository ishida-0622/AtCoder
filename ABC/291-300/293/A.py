s=input()
ans=""
for i in range(len(s)//2):
    ans+=s[i*2+1]+s[i*2]
print(ans)
