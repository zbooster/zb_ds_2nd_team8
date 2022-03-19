import random

students = [random.randint(170, 185) for i in range(20)]
print(f'students: {students}')

length = len(students) - 1
for i in range(length):
    for j in range(length - i):
        if students[j] > students[j + 1]:
            students[j], students[j + 1] = students[j + 1], students[j]

print(f'students: {students}')


