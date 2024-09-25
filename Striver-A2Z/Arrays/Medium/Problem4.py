# Kadane's Algorithm : Maximum Subarray Sum in an Array

# <=================================BRUTH FORCE==================================>

# def maxSum(arr):
#     maxi=float("-inf")
#     for i in range(len(arr)):
#         sum=0
#         for j in range(i, len(arr)):
#             sum+=arr[j]
#             maxi=max(maxi,sum)
#     return maxi
# arr=[-2,1,-3,4,-1,2,1,-5,4]
# print(maxSum(arr))

# <=================================OPTIMUM APPROACH==================================>

def maxSum(arr):
    maxi=float("-inf")
    currSum=0
    for i in range(len(arr)):
        currSum+=arr[i]
        if currSum>maxi:
            maxi=currSum
        if currSum <0:
            currSum=0
    return maxi
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSum(arr))


