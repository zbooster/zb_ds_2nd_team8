num1 = 10
num2 = 100

numResult = True if num1 > num2 else False
print('num1 > num2 : {}'.format(numResult))

print('num1은 num2 보다 크다.') if numResult else print('num1은 num2보다 크지 않다.')

# limitSnowAmount = 30
# snowAmount = int(input('적설량 입력(mm) : '))
# print('적설량: {}mm, {}'.format(snowAmount, '대설 경보 발령!!')) if snowAmount > limitSnowAmount else \
#     print('적설량: {}mm, {}'.format(snowAmount, '대설 경보 해제~~'))

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

print('국어 : ', end='')
print('PASS') if kor >= 60 else print('FAIL')
print('영어 : ', end='')
print('PASS') if eng >= 60 else print('FAIL')
print('수학 : ', end='')
print('PASS') if mat >= 60 else print('FAIL')

avg = (kor + eng + mat) / 3
print('시험 : ', end='')
print('PASS') if mat >= 70 else print('FAIL')

print('총점 : %d, 평균 : %.2f' % ((kor+eng+mat), avg))

