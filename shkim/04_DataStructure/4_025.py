# students = ('홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동')
# print('students: {}'.format(students))
#
# print('students: {}'.format(students[2:4]))
# print('students: {}'.format(students[:4]))
# print('students: {}'.format(students[2:]))
# print('students: {}'.format(students[2:-2]))
# print('students: {}'.format(students[-5:-2]))

# students = ('홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동')
# print('students: {}'.format(students))
#
# students[1:4] = ('park', 'lee', 'kim')
# print('students: {}'.format(students))
# Traceback (most recent call last):
#   File "C:\pythonEx\zb_ds_2nd_team8\shkim\04_DataStructure\4_025.py", line 13, in <module>
#     students[1:4] = ('park', 'lee', 'kim')
# TypeError: 'tuple' object does not support item assignment
# students: ('홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동')

students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
print('students: {}'.format(students))

students[1:4] = ('park', 'lee', 'kim')
print('students: {}'.format(students))