# cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'
#
# for i in range(len(cars)):
#     print(cars[i])
#
# for car in cars:
#     print(car)

studuntCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

sum = 0
for classNo, cnt in studuntCnts:
    print('{}학급 학생수: {}명'.format(classNo, cnt))
    sum += cnt

avg = sum / len(studuntCnts)

print('전체 학생 수: {}명'.format(sum))
print('평균 학생 수: {}명'.format(avg))