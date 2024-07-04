# Find Array are sorted or not?

def sorted(arr, size):
    if size <= 1:
        return True
    
    if arr[0] > arr[1]:
        return False
    
    return sorted(arr[1:], size - 1)

arr = [1, 2, 3, 4, 5]
size = len(arr)
print(sorted(arr, size))

