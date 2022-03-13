# from arithmetic import basic_operator as bo
# from arithmetic import developer_operator as do
#
# num1 = float(input('숫자1 입력: '))
# num2 = float(input('숫자2 입력: '))
#
# bo.add(num1, num2)
# bo.sub(num1, num2)
# bo.mul(num1, num2)
# bo.div(num1, num2)
#
# do.mod(num1, num2)
# do.flo(num1, num2)
# do.pow(num1, num2)

# from shape import triangle_square_area as ts
#
# width = float(input('가로 길이 입력: '))
# height = float(input('세로 길이 입력: '))
#
# ts.triangleArea(width, height)
# ts.squareArea(width, height)

from shape import circle_area as ca

radius = float(input('반지름 입력: '))

ca.circleArea(radius)