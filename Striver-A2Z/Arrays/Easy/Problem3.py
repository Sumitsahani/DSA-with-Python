# Check if an Array is Sorted

def checkSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print("Not sorted")
            return
    print("It's sorted")

arr = [1, 2, 3, 4, 5]
checkSorted(arr)
