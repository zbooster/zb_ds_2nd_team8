# def calculator(n1, n2):
#     result = n1 + n2
#     return result
#
# # returnValue = calculator(10, 20)
# # print(f'returnValue : {returnValue}')
#
# def divideNumber(n):
#     if n % 2 == 2:
#         return '짝수'
#     else:
#         return '홀수'
#
# print(f'{1}은 {divideNumber(1)}입니다.')
#
# def convertToMm(x):
#     return x * 10
#
# lengthCm = float(input('길이(cm)입력: '))
# print(f'returnValue: {convertToMm(lengthCm)}mm')

import random

def returnOdd():
    r = 0
    while True:
        r = random.randint(1, 100)
        if r % 2 == 1:
            break
    return r

print(f'returnValue: {returnOdd()}')