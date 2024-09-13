# Left Rotate the Array by One
def leftRotate(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp

arr = [1, 2, 2, 3, 3]
leftRotate(arr)
print(arr)

        