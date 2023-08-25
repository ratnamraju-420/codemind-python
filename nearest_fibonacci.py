i=int(input())
f=0
s=1
n=0
while(i>n):
    n=f+s
    f=s
    s=n
if(i-f<s-i):
    print(f)
elif(i-f==s-i):
    print(f,s)
else:
    print(s)
    

