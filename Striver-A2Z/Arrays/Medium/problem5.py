# Print subarray with maximum subarray sum (extended version of above problem)

def maxSum(arr):
    maxi = float("-inf")
    currSum = 0
    start = end = s = 0
    
    for i in range(len(arr)):
        currSum += arr[i]

        if currSum > maxi:
            maxi = currSum
            start = s
            end = i
        
        if currSum < 0:
            currSum = 0
            s = i + 1

    return maxi, arr[start:end+1]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = maxSum(arr)
print(max_sum)
print(*subarray)
