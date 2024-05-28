N,K=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(N):
    swapped = False
    for j in range(0, N-i-1):
        if arr[j] % K > arr[j+1] % K or arr[j]%K==arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            swapped = True
    if not swapped:
        break
print(*arr)