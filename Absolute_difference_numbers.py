n,x=map(int,input().split())
a=str(n)
print(abs(int(a[:x])-int(a[len(a)-x:])))