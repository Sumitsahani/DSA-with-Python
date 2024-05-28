n = int(input())
students = []

for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    students.append((name, marks))

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if (students[j][1] < students[j+1][1]) or (students[j][1] == students[j+1][1] and students[j][0] > students[j+1][0]):
                students[j], students[j+1] = students[j+1], students[j]
    return students

sorted_students = bubble_sort(students)
ranked_students = []
current_rank = 1

for i in range(n):
    if i > 0 and sorted_students[i][1] < sorted_students[i-1][1]:
        current_rank = i + 1
    ranked_students.append((sorted_students[i][0], current_rank))

for student in ranked_students:
    print(student[1], student[0])
