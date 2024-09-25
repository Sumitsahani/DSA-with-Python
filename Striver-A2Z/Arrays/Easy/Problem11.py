# Find the number that appears once, and the other numbers twice
def AppearsOnce(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    
    for key, value in dic.items():
        if value == 1:
            return key

arr = [1, 2, 3, 4, 2, 3, 4]
print(AppearsOnce(arr))
