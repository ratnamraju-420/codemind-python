n=int(input())
z=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in z:
    if(i<a or i>b):
        s=s+i
print(s)