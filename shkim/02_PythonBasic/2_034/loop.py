import random

sum = 0
day = 0
flag = True

while flag:
    day += 1
    patientNum = random.randint(50, 100)
    sum += patientNum
    if sum > 10000:
        flag = False
    print('날짜 : {}, 오늘 환자수 : {}, 누적 환자수 : {}'.format(day, patientNum, sum))

