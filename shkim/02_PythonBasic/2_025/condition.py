# 비올 확률을 입력하고 비올 확률이 55% 이상이면 '우산을 챙기세요'를 그렇지 않으면
# '양산을 챙기세요.' 출력하는 코드를 작성하자.

# rainPercentage = int(input('비올 확률 입력 : '))
#
# if rainPercentage >= 55:
#     msg = '우산'
# else:
#     msg = '양산'
#
# print('{}을 챙기세요.'.format(msg))

minTemperatures = int(input('최저 기온 입력 : '))
maxTemperatures = int(input('최고 기온 입력 : '))

diffTemperatures = maxTemperatures - minTemperatures

if diffTemperatures >= 11:
    print('일교차: {}도'.format(diffTemperatures))
    print('감기 조심하세요.')
else:
    print('일교차: {}도'.format(diffTemperatures))
    print('산책하기 좋은 날씨입니다.')

