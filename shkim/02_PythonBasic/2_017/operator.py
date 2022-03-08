num1 = 10

num1 += 3
print('num1 : {}'.format(num1))

num1 -= 3
print('num1 : {}'.format(num1))

num1 *= 3
print('num1 : {}'.format(num1))

num1 /= 3
print('num1 : {}'.format(num1))

num1 **= 3
print('num1 : {}'.format(num1))

num1 //= 3
print('num1 : {}'.format(num1))

num1 %= 3
print('num1 : {}'.format(num1))

monthRain = (30, 45, 47, 55, 65, 100, 128, 209, 204, 186, 67, 25)
totalRain = 0

for month in range(0, 12):
    totalRain += monthRain[month]
    print(f'{(month+1)}월 누적 강수량 : {totalRain:,}mm')

print('-' * 30)
print(f'연간 누적 강수량 : {totalRain:,}mm')
print('연간 평균 강수량 : %.2f' % (totalRain/12))
print('-' * 30)


