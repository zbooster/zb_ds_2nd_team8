# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
# print('students: {}'.format(students))
#
# print('students: {}'.format(students[2:4]))
# print('students: {}'.format(students[:4]))
# print('students: {}'.format(students[2:]))
# print('students: {}'.format(students[2:-2]))
# print('students: {}'.format(students[-5:-2]))

# numbers = [2, 50, 0.12, 1, 9 , 7, 17, 35, 100, 3.14]
# print('numbers: {}'.format(numbers))
# print('numbers: {}'.format(numbers[2:-2]))
# print('numbers: {}'.format(numbers[2:-2:2]))
# print('numbers: {}'.format(numbers[:-2:2]))
# print('numbers: {}'.format(numbers[::2]))

students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
print('students: {}'.format(students))

students[1:4] = ['park', 'lee', 'kim']
print('students: {}'.format(students))

students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
print('students: {}'.format(students))

print('students: {}'.format(students[slice(2, 4)]))
print('students: {}'.format(students[slice(4)]))
print('students: {}'.format(students[slice(2, len(students))]))
print('students: {}'.format(students[slice(2, len(students)-2)]))
print('students: {}'.format(students[slice(len(students)-5, len(students)-2)]))
