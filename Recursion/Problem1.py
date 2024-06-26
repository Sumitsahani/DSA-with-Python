def fact(n):
    if n == 0:
        return 1
    else:
        smallProblem = fact(n - 1)
        biggerProblem = n * smallProblem
        return biggerProblem

print(fact(3))
