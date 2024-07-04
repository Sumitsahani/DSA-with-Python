# K presant in arr or not

def ArrK(arr, size,k):
    if size==0:
        return False
    if arr[0]==k:
        return True
    else:
        return ArrK(arr[1:],size-1,k)

arr=[1,2,3,42,3]
k=0
size=len(arr)
print(ArrK(arr, size,k))