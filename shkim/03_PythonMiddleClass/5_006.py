# def printArea():
#     triangleArea = width * heigth / 2
#     squareArea = width * heigth
#
#     print(f'삼각형 넓이: {triangleArea}')
#     print(f'사각형 넓이: {squareArea}')
#
# width = int(input('가로 길이 입력: '))
# heigth = int(input('세로 길이 입력: '))
# printArea()

totalVisit = 0

def countTotalVisit():
    global totalVisit

    totalVisit = totalVisit + 1
    print(f'누적 방문객: {totalVisit}')

countTotalVisit()
countTotalVisit()
countTotalVisit()
countTotalVisit()
countTotalVisit()
