def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

n,m = mapInt()
lst = [[0,i+1] + list(input()) for i in range(n*2)]
for i in range(m):
    for j in range(1,n+1):
        a = lst[j*2-2][2+i]
        b = lst[j*2-1][2+i]
        if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
            lst[j*2-2][0] -= 1
        if (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
            lst[j*2-1][0] -= 1
    lst.sort()

for i in lst:
    print(i[1])