# sum of series
# End
# Description
# Given two integers N, X. Find the value of the series: 1 + x + x*x + x*x*x + x*x*x*x +-------N the term WhereN is the no. of term,
# X contains the value of x.
# Note: If N <= 0 or X <= 0 print -1
# For Example
# • Give N = 3, X = 2
# We need to find the sum of first N=3 terms, having value of X=2 First 3 terms in Expression = 1 + x + x*x = 1+ 2+ 2*2 = 7 Answer is 7

def solve(N, X):
    if N<=0 or X<=0:
        print(-1)
    else:
        sum=1
        power=1
        for i in range(1, N):
            power*=X
            sum+=power
        print(sum)
        
N,X=map(int,input().split())
solve(N,X)