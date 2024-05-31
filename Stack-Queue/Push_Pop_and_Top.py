# Description

# There is a stack of integers which is currently empty. You are given an integer n and there are n operations that you need to perform on the stack

# The next n line contains one of the following 3 operations

# 1: Push x to the top of the stack

# 2: Pop an element from the top of the stack. If the stack is empty, do nothing.

# 3: Print the top element of the stack (if stack is empty, print "Empty!" (without quotes)).

# For better understanding, read sample test case explanation

# Input

# Input Format:

# First line of test case contains n

# In the next in lines there can be one of the following three possible inputs:

# 1 separated by an integer; In that case, you have to push that integer to stack

# 2: Pop an element from the top of the stack. If the stack is empty, do nothing

# 3: Print the top element of the stack (see Output Format).

# Constraints:

# N-1000

# Output

# Whenever the query (out of the n queries) is 3, print top element of stack.

# Input:                       Output:
# 6                            15
# 1 15                         Empty!
# 1 20
# 2
# 3
# 2
# 3



N=int(input())
operation = [input().strip() for i in range(N)]

stack=[]
result=[]

for i in operation:
    op=i.split()
    if op[0]=="1":
        stack.append(op[1])
    if op[0]=="2":
        if stack:
            stack.pop()
    if op[0]=="3":
        if not stack:
            result.append("Empty!")
        else:
            result.append(str(stack[-1]))
print("output:")
for i in result:
    print(i)

     

