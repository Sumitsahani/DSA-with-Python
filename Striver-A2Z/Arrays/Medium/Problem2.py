def zeroOneTwo(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1
    
    return arr
arr = [0, 1, 2, 1, 0, 2, 1, 0]
sorted_arr = zeroOneTwo(arr)
print(sorted_arr)
