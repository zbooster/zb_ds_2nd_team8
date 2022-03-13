# baseTemp = 29
# height = int(input('고도 입력:'))
#
# print('지면 온도: {}'.format(baseTemp))
# targetTemp = baseTemp - (height // 60) * 0.8
# print('고도 {}m의 기온: {}'.format(height, round(targetTemp, 1)))

bread = 197
milk = 152
studuntNum = 17

print('학생 한명이 갖게되는 빵 개수: {}'.format(bread // studuntNum))
print('학생 한명이 갖게되는 우유 개수: {}'.format(milk // studuntNum))
print('남는 빵 개수: {}'.format(bread % studuntNum))
print('남는 우유 개수: {}'.format(milk % studuntNum))