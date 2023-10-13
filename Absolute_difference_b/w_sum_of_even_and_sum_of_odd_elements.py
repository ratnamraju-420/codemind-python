n=int(input())
l1=list(map(int,input().split()))
os=0
es=0
for i in l1:
    if(i%2!=0):
        os+=i
    if(i%2==0):
        es+=i
if(os>es):
    print(os-es)
else:
    print(es-os)
    