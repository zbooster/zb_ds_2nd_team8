students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
print('students: {}'.format(students))

searchCnt = students.count('강호동')
print('searchCnt: {}'.format(searchCnt))

del students[2:]
print('students: {}'.format(students))

import random

types = ['A', 'B', 'AB', 'O']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

#print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for type in types:
    print('{}\t: {}개'.format(type, todayData.count(type)))