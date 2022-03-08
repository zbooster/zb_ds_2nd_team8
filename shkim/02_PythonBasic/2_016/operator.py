num1 = 2
num2 = 3

result = num1 ** num2
print('result : {}'.format(result))

# 2의 제곱근
result = 2 ** (1/2)
print('2의 제곱근 %f' % result)
print('2의 제곱근 %.2f' % result)

import math

print('2의 제곱근: {}'.format(math.sqrt(2)))

firstMonthMoney = 200
after12Month = firstMonthMoney * (2 ** (12-1))

print('12개월 후 용돈 : {}'.format(after12Month))
print(f'12개월 후 용돈 : {after12Month:,}')


