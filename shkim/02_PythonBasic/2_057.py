userNum = int(input('정수 입력: '))

sum = 0
sumEven = 0
sumOdd = 0
sumFac = 1
for i in range(1, 1+userNum):
    if i % 2 == 0:
        sumEven += i
    else:
        sumOdd += i
    sum += i
    sumFac *= i

print('합 결과: {}'.format(sum))
print('홀수 합 결과: {}'.format(sumOdd))
print('짝수 합 결과: {}'.format(sumEven))
print('팩토리얼 결과: {}'.format(format(sumFac, ',')))

