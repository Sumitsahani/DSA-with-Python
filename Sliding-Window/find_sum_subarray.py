# Given in Array find max sum of all subarrays of of size K ?

# first find start subarrays sum whose size K
import math
Subarrays_sum =0
i=0
K=4
arr=[1,4,2,10,23,3,1,0,20]
for i in range(K):
    Subarrays_sum+=arr[i]
res =Subarrays_sum
# second is start k index to less then n-1 and calculate sum with subtract 1 array and add k value means arr[i] value
for i in range(K,len(arr)):
    Subarrays_sum=Subarrays_sum-arr[i-K]+arr[i]    #arr[i-K] is arr[5-4] =1 and arr[i]=arr[5] =23 
    res = max(res,Subarrays_sum);
print(res)
