n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

print(*arr)