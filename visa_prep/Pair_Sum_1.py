n=int(input())
arr=list(map(int,input().split()))
k=int(input())
found=False
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k and i<j:
            found=True
            break
if found:
    print('true')
else:
    print('false')
