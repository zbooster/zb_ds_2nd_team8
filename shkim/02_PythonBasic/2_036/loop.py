# result = 1
#
# for i in range(1, 11):
#     result *= i
#     print('num : {}, result : {}'.format(i, result))
#
#     if result > 50:
#         print('결과값이 50이 넘어갈 때 숫자 : {}'.format(i))
#         break

dogWeight = 800
eatNum = 0

while True:
    eatNum += 1
    dogWeight += 70

    if dogWeight > 2200:
        print('이유식 중단 날짜 : {}'.format(eatNum))
        break
