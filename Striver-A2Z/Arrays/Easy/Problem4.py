# Remove Duplicates in-place from Sorted Array
def isSorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            print("not sorted")
            return
    print("sorted")

arr = [1, 2, 2, 3, 4, 5, 5]
isSorted(arr)
