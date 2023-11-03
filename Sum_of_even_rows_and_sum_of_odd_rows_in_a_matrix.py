r, c =map(int,input().split())
mat=[list(map(int,input().split()))[:c:] for i in range(r)]
s1 = 0
s2 = 0
for i in range(0,r):
    if i%2==0:
        s1+=sum(mat[i])
    else:
        s2+=sum(mat[i])
print(s1, s2)
            