# cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']
#
# n = 0
# while n < len(cars):
#     print(cars[n])
#     n += 1
#
# n = 0
# flag = True
# while flag:
#     print(cars[n])
#     n += 1
#
#     if n == len(cars):
#         flag = False
#
# n = 0
# while True:
#     print(cars[n])
#     n += 1
#
#     if n == len(cars): break

studuntCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

sum = 0

n = 0
while n < len(studuntCnts):
    classNo = studuntCnts[n][0]
    cnt = studuntCnts[n][1]
    sum += cnt
    print('{}학급 학생수: {}명'.format(classNo, cnt))
    n += 1

avg = sum / len(studuntCnts)
print('전체 학생 수: {}명'.format(sum))
print('평균 학생 수: {}명'.format(avg))

