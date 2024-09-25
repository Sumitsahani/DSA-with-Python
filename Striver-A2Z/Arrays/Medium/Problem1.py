# Two Sum : Check if a pair with given sum exists in Array

def twoSum(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == k:
            print("Yes")
            return
        elif arr[left] + arr[right] < k:
            left += 1
        else:
            right -= 1
    print("No")

arr = [1, 2, 4, 1]
k = 5
twoSum(arr, k)

        