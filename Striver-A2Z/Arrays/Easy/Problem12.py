# Longest Subarray with given Sum K(Positives)

def logSubarr(arr):
    sum=0
    for i in range(len(arr)):
        sub=[]
        for j in range(i,len(arr)):
            sub+=arr[j]
            sum+=sub
    return sum
arr=[1,2,3,2,1]
print(logSubarr(arr))
