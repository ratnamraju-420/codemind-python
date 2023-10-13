n=int(input())
l1=list(map(int,input().split()))
for i in range(len(l1)):
    if l1[i]%2==0:
        last=i
print(last)