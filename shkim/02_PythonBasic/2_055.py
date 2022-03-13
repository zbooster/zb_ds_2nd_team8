# import random
#
# comNum = random.randint(1, 1000)
#
# n = 0
# while True:
#     userNum = int(input('1에서 1000까지 정수 입력: '))
#     n += 1
#     if comNum == userNum:
#         break
#     elif comNum > userNum:
#         print('난수가 크다!')
#     else:
#         print('난수가 작다!')
#
# print('난수: {}, 시도 횟수: {}'.format(comNum, n))

inRoomTemp = int(input('실내온도 입력: '))
autoOper = ''

if inRoomTemp <= 18:
    autoOper = 'OFF'
elif (inRoomTemp > 18) and (inRoomTemp <= 22):
    autoOper = '매우 약'
elif (inRoomTemp > 22) and (inRoomTemp <= 24):
    autoOper = '약'
elif (inRoomTemp > 24) and (inRoomTemp <= 26):
    autoOper = '중'
elif (inRoomTemp > 26) and (inRoomTemp <= 28):
    autoOper = '강'
elif inRoomTemp > 28:
    autoOper = '매우 강'

print('에어컨: {}!!'.format(autoOper))