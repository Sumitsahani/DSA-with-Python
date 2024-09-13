arr = [1, 2, 1, 4, 2]
maximum = arr[0]

for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print(maximum)
