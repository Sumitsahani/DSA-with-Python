# check key value present in array or not

def checkKey(arr, start, end, key):
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if arr[mid] == key:
        return 1

    if arr[mid] < key:
        return checkKey(arr, mid + 1, end, key)
    else:
        return checkKey(arr, start, mid - 1, key)

arr = [1, 3, 2, 4, 51]
size = 5
key = 4

print(checkKey(arr, 0, size - 1, key))

    
