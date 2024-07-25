# Description
# You are given a number R. Find the value of R, after doing the following operations:-
# 1. R is multiplied by 7
# 2. 15 is added in the new value of R.
# 3. 5 is subtracted from the new value of R.
# 4. R is divided by 2 (print floor value).
# ----------------------------------------------------------------------------------------------
# Hint
# In the sample input R = 2, the following operations will look like thi s:-
# 1. R is multiplied by 7 R = 2 * 7 -> 14
# 2. 15 is added in the new value of R. ->R15+ 14 -> 29
# 3. 5 is subtracted from the new value of R. R = 29 - 5 -> 24
# 4. R is divided by 2 (print floor value). -> R 24/2 12


def findR(r):
    multi =r*7
    add=multi+15
    sub=add-5
    div=sub//2
    print(div)

r=int(input())
findR(r)
