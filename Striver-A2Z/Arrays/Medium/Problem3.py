# Find the Majority Element that occurs more than N/2 times
def OccursMore(arr):
    dic={}
    for i in range(len(arr)):
        if i in dic:
            dic[arr[i]]+=1
        else:
            dic[arr[i]]=1
    for key,value in dic.items():
        if value <=len(arr)-1//2:
            return key
arr=[2,3,2]
print(OccursMore(arr))