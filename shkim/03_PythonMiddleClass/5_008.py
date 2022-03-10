# def calculator(n1, n2):
#     return n1 + n2
#
# returnValue = calculator(10, 20)
# print(f'returnValue: {returnValue}')
#

# calculator = lambda n1, n2: n1 + n2
# returnValue = calculator(10, 20)
# print(f'returnValue: {returnValue}')

getTriangleArea = lambda n1, n2: n1 * n2 / 2
getSquareArea = lambda n1, n2: n1 * n2
getCircleArea = lambda radius : radius * radius * 3.14

width = int(input('가로 길이 입력: '))
heigth = int(input('세로 길이 입력: '))
radius = int(input('반지름 길이 입력: '))

print(f'삼각형 넒이: {getTriangleArea(width, heigth)}')
print(f'사각형 넒이: {getSquareArea(width, heigth)}')
print(f'원 넓이: {getCircleArea(radius)}')

