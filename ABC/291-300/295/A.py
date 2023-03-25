def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()

a = ["and", "not", "that", "the", "you"]
n = int(input())
lst = input().split()
for v in lst:
    if v in a:
        yes()
no()
