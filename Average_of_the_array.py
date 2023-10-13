n=int(input())
l1=list(map(int,input().split()))
s=0
for i in l1:
    s+=i
Avg=s/n    
print("%.2f"%Avg)    