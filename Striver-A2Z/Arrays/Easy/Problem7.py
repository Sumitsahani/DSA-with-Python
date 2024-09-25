# Move all Zeros to the end of the array
def MoveZero(arr):
    temparr = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temparr.append(arr[i])
    for j in range(len(arr)):
        if arr[j] == 0:
            temparr.append(0)
    for k in range(len(arr)):
        arr[k] = temparr[k]

arr = [1, 3, 0, 0, 1, 2]
MoveZero(arr)
print(*arr)
