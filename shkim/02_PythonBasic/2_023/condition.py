if 10 > 5:
    print('10은 5보다 크다.')
    print('또 다른 실행문 !!')

print('조건문이 끝났어요.')

# korScore = int(input('국어 점수 입력 : '))
# engScore = int(input('영어 점수 입력 : '))
# matScore = int(input('수학 점수 입력 : '))
#
# avg = (korScore + engScore + matScore) / 3
#
# print('평균 : %.1f' % avg)
# if avg >= 90:
#     print('참 잘했어요~')

highTemperature = 28
lowerTemperature = 20

innerTemperature = int(input('실내 온도 입력 : '))

if innerTemperature >= 28:
    print('냉방 작동!')
elif innerTemperature <= 20:
    print('난방 작동!')

