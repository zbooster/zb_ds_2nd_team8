# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철']
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# # print(students[5])
#
# numbers = [10, 20, 30, 40, 50, 60, 70]
# print(type(numbers[0]))
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

students = ['김성예', '신경도', '박기준', '최승철', '황동석']
print('-- 인덱스가 짝수인 학생 --')
print('students[0] : {}'.format(students[0]))
print('students[2] : {}'.format(students[2]))
print('students[4] : {}'.format(students[4]))
print('-- 인덱스가 홀수인 학생 --')
print('students[1] : {}'.format(students[1]))
print('students[3] : {}'.format(students[3]))

for i in range(5):
    if i % 2 == 0:
        print('인덱스 짝수 : students[{}] : {}'.format(i, students[i]))
    else:
        print('인덱스 홀수 : students[{}] : {}'.format(i, students[i]))

