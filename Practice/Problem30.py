def solve(N, arr):
    oddSum=0
    evenSum=0
    for i in arr:
        if i%2==0:
            evenSum+=i
        else:
            oddSum+=i
    print(evenSum-oddSum)

N=4
arr=[1,2 ,3, 4]
solve(N,arr)