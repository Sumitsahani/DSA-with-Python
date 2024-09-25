# Count Maximum Consecutive One's in the array
def MaxCon(arr):
    maximum = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0
    return maximum
arr = [1, 0, 1, 1, 0, 1]
print(MaxCon(arr))
