# sum = 0
#
# maxInt = 0
#
# for i in range(1, 101):
#     if i % 7 == 0 and sum <= 50:
#         sum += i
#         maxInt = i
#
#     print('i : {}'.format(i))
#
# print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(maxInt))

tireThick = 30
circleNum = 0

while tireThick >= 20:
    tireThick -= 0.15
    circleNum += 1

print('운행 가능 횟수 : {}'.format(circleNum - 1))