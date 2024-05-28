n = int(input())
arr = list(map(int, input().split()))
newArr = []
current_max =0
for i in arr:
    if i >= current_max:
        newArr.append(i)
        current_max = i
print(*newArr)
