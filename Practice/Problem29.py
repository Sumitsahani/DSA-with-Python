# Happy number

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# • Starting with any positive integer, replace the number by the sum of the squares of its digits.
# • Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# • Those numbers for which this process ends in 1 are happy.
# Input
# Input Format
# The first line contains an integer t - the number of testcases.
# The next t lines contain the description of the t testcases.
# The first and only line of each testcase contains an integer n.


def happyNum(num):
    i=0
    while(i<10):
        sum=0
        while(num!=0):
            rem=num%10
            sum+=rem**2
            num=num//10
        if sum==1:
            print("Yes")
            break
        else:
            num=sum
        i+=1
    else:
        print("No")

happyNum(2)
