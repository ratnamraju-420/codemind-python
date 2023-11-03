r, c =map(int,input().split())
mat=[]
for i in range(r):
    inner_list = list(map(int,input().split()))[:c:]
    mat.append(inner_list)
s1 = 0
s2 = 0
for inner_list in mat:
    for E in inner_list:
        if(E%2==0):
            s1+=E
        else:
            s2+=E
print(s1, s2)        
