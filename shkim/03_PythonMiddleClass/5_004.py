# def greet(customer):
#     print('{}님 안녕하세요.'.format(customer))
#
# greet('홍길동')
# greet('박찬호')
#
# def calculator(n1, n2):
#     print(f'{n1} + {n2} = {n1+n2}')
#     print(f'{n1} - {n2} = {n1-n2}')
#     print(f'{n1} x {n2} = {n1*n2}')
#     print(f'{n1} / {n2} = {n1/n2}')
#
# calculator(3, 5)
#
#
# def printNumber(*number):
#     print(type(number))
#
# printNumber()

def printScore(kor, eng, mat):
    sum = kor+eng+mat
    print('총점 : {}'.format(sum))
    print('평균 : %.2f' % (sum / 3))

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))

printScore(kor, eng, mat)
