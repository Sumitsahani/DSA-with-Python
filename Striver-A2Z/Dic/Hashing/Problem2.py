# Find the highest/lowest frequency element
def solve(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    mini=float('inf')
    maxi=float('-inf')
    for key,value in d.items():
        if value>maxi:
            maxi=key
        if value<mini:
            mini=key
    print(mini)
    print(maxi)
arr=[10,5,10,15,10,51]
solve(arr)