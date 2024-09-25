# Linear Search

def linerSearch(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
arr=[1,3,2,5,6]
k=5
res=linerSearch(arr,k)
print(res)
