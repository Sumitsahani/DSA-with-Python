# Second Largest Element in an Array without sorting
def find_second_largest(arr): 
    largest = float('-inf')
    second_largest = float('-inf') 
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num   
    return second_largest
arr = [10, 5, 20, 8, 30]
result = find_second_largest(arr)
print(result)
