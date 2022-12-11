s=input()
AZ="QWERTYUIOPASDFGHJKLZXCVBNM"
try:
    n=int(s[1:-1])
    if len(s)==8 and s[0] in AZ and s[-1] in AZ and 100000 <= n <= 999999:
        print("Yes")
    else:
        print("No")
except:
    print("No")
