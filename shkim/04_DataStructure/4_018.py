# students = ['홍길동', '박찬호', '이용규']
# print('students: {}'.format(students))
#
# students *= 2
# print('students: {}'.format(students))
#
#
# students = ['홍길동', '강호동', '이용규', '김지은', '박승철', '강호동']
# print('students: {}'.format(students))
# print('강호동의 index: {}'.format(students.index('강호동')))
# print('강호동의 index: {}'.format(students.index('강호동', 2, 6)))

import random

sampleList = random.sample(range(1, 11), 10)

selectIdx = int(input('숫자 7의 위치 입력: '))
searchIdx = sampleList.index(7)

if selectIdx == searchIdx:
    print('빙고')
else:
    print('실패')

print('sampleList: {}'.format(sampleList))
print('searchIdx: {}'.format(searchIdx))