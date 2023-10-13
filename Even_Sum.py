n=int(input())
l1=list(map(int,input().split()))
s=0
for i in l1:
    if(i%2==0):
        s+=i
print(s)        