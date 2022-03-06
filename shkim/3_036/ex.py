inputA1 = int(input('a1입력: '))
inputD = int(input('공차입력: '))
inputN = int(input('n입력: '))
#
# valueN = 0; sumN = 0
# n = 1
# while n <= inputN:
#     if n == 1:
#         valueN = inputA1
#         sumN += valueN
#         print('{}번째 항의 값: {}'.format(n, valueN))
#         print('{}번째 항의까지의 합: {}'.format(n, sumN))
#         n += 1
#         continue
#
#     valueN += inputD
#     sumN += valueN
#     print('{}번째 항의 값: {}'.format(n, valueN))
#     print('{}번째 항의까지의 합: {}'.format(n, sumN))
#     n += 1
#
# print('{}번째 항의 값: {}'.format(inputN, valueN))
# print('{}번째 항의까지의 합: {}'.format(inputN, sumN))

#an = a1 + (n-1)*d
valueN = inputA1 + (inputN-1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))

#sn = n*(a1 + an) / 2
sumN = inputN * (inputA1 + valueN) / 2
print('{}번째 항의까지의 합: {}'.format(inputN, int(sumN)))
