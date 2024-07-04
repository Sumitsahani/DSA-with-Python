# Sum Of Array

def sumArr(arr, size):
    if size == 0:
        return 0
    if size == 1:
        return arr[0]
    else:
        return arr[0] + sumArr(arr[1:], size - 1)

arr = [1]
size = len(arr)
print(sumArr(arr, size))
