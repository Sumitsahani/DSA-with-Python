# Rearrange Array Elements by Sign
# Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

def rearrange_by_sign(arr, N):
    positive = []
    negative = []
    
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    
    result = [0]*N
    pos_index = 0
    neg_index = 0
    
    for i in range(N):
        if i % 2 == 0:
            if pos_index < len(positive):
                result[i] = positive[pos_index]
                pos_index += 1
        else:
            if neg_index < len(negative):
                result[i] = negative[neg_index]
                neg_index += 1
    return result

arr = [1,2,-3,-1,-2,-3]
N = 6
output = rearrange_by_sign(arr, N)
print(output)
