# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철']
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# students.append('강호동')
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# scores = [['국어', 88],
#           ['영어', 91]]
#
# print('scores: {}'.format(scores))
# print('scores의 길이: {}'.format(len(scores)))
# print('last index : {}'.format(len(scores) - 1))
#
# scores.append(['수학', 96])
# print('scores: {}'.format(scores))
# print('scores의 길이: {}'.format(len(scores)))
# print('last index : {}'.format(len(scores) - 1))

myFamilyAge = [['아빠', 40], ['엄마', 38], ['나', 9]]
myFamilyAge.append(['동생', 1])

for name, age in myFamilyAge:
    print('{}의 나이: {}'.format(name, age))