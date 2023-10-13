n=int(input())
l1=list(map(int,input().split()))
s=0
for i in l1:
    s+=i
Avg=s//n
if Avg in l1:
    print("True")
else:
    print("False")