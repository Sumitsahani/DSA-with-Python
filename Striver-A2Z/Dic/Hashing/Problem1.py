def countElement(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    print(dic)

arr = [1, 3, 2, 2, 3, 2]
countElement(arr)
