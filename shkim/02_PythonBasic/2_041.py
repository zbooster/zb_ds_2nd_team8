# inputStr = input('메시지 입력: ')
#
# print('메시지 문자열 길이 : {}'.format(len(inputStr)))

# str = '파이썬은 1991년 네덜란드계 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 대화형 언어이다. 파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'
# print('\'객체지향\' 문자열 위치: {}'.format(str.find('객체지향')))

num1 = float(input('가로 길이 입력: '))
num2 = float(input('세로 길이 입력: '))

print('-'*10, 'Result', '-'*10)
print('삼각형 넓이 : %.6f' % (num1 * num2 / 2))
print('사각형 넓이 : %.6f' % (num1 * num2))
print('삼각형 넓이 : %.2f' % (num1 * num2 / 2))
print('사각형 넓이 : %.2f' % (num1 * num2))
print('-'*28)
