n=int(input())
odd=0
arr=list(map(int,input().split()))
for i in range(n):
	if(arr[i]%2!=0):
		odd+=1;
if(odd<=2):
	print("YES");
else:
	print("NO")