str = 'Hi '
result = str * 5

print('result : {}'.format(result))

num1 = 10
num2 = 3

result = num1 / num2

print('result : {}'.format(result))
print('result : %.2f' % result)

num1 = 0
num2 = 3

result = num1 / num2

print('result : {}'.format(result))
print('result : %.2f' % result)

# 0으로 나누는 경우, ZeroDivisionError: division by zero
# num1 = 10
# num2 = 0
#
# result = num1 / num2
#
# print('result : {}'.format(result))
# print('result : %.2f' % result)

num1 = 20
num2 = 5

result = num1 / num2

print('result : {}'.format(result))
print('type of result : {}'.format(type(result)))

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

print('국어 점수 {}'.format(kor))
print('영어 점수 {}'.format(eng))
print('수학 점수 {}'.format(mat))

total = kor + eng + mat
print('합계 {}'.format(total))

avg = total / 3
print('평균 {}'.format(avg))
print('평균 %.2f' % avg)

