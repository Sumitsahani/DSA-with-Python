test =int(input())
for i in range(test):
    N,K=map(int, input().split())
    A=list(map(int, input().split()))
    subarray_sum=0
    high=0
    for i in range(N):
        while subarray_sum<K and high<N:
            subarray_sum+=A[high]
            high+=1
        if subarray_sum==K:
            print("Yes")
            break
        subarray_sum-=A[i]
    else:
        print("No")
        
            
    