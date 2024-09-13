def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = a[l + i]
    for j in range(n2):
        R[j] = a[m + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    # Merge the temp arrays back into a[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def mergesort(a, l, r):
    if l < r:
        # Find the middle point
        m = l + (r - l) // 2

        # Sort first and second halves
        mergesort(a, l, m)
        mergesort(a, m + 1, r)

        # Merge the sorted halves
        merge(a, l, m, r)

# Input size of array and elements
n = int(input())
a = list(map(int, input().split()))

# Call mergesort function
mergesort(a, 0, n - 1)

# Print the sorted array
print(*a)
