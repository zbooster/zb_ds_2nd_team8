inputA1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

# valueN = 0
# sumN = 0
# n = 1
# while n <= inputN:
#     if n == 1:
#         valueN = inputA1
#         sumN = valueN
#         print('{}번째의 값: {}'.format(n, valueN))
#         print('{}번까지의 합: {}'.format(n, sumN))
#         n += 1
#         continue
#
#     valueN *= inputR
#     sumN += valueN
#     print('{}번째의 값: {}'.format(n, valueN))
#     print('{}번까지의 합: {}'.format(n, sumN))
#     n += 1
#
# print('{}번째의 값: {}'.format(inputN, valueN))
# print('{}번까지의 합: {}'.format(inputN, sumN))

# an = a1 * r^(n-1)
valueN = inputA1 * (inputR ** (inputN-1))
print('{}번째의 값: {}'.format(inputN, valueN))

# sn = a1 * (1-r^n) / (1-r)
sumN = inputA1 * (1 - inputR**inputN) / (1-inputR)
print('{}번까지의 합: {}'.format(inputN, int(sumN)))