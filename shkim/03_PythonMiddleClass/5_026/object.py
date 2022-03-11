# class Robot:
#
#     def __init__(self, c, h, w):
#         self.color = c
#         self.height = h
#         self.weight = w
#
#     def fire(self):
#         print('미사일 발사!!')
#
#     def printRobotInfo(self):
#         print(f'self.color: {self.color}')
#         print(f'self.height: {self.height}')
#         print(f'self.weight: {self.weight}')
#
#
# class NewRobot(Robot):
#
#     def __init__(self, c, h, w):
#         super().__init__(c, h, w)
#
#     def fire(self):
#         print('레이저 발사!!!')
#
#
# myRobot = NewRobot('red', 200, 300)
# myRobot.printRobotInfo()
# myRobot.fire()
class TriangleArea:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTriangleAreaInfo(self):
        print(f'self.width: {self.width}')
        print(f'self.height: {self.height}')

    def getArea(self):
        return self.width * self.height / 2


class NewTriangleArea(TriangleArea):

    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        area = str(super().getArea())
        return area + 'cm2'


ta = NewTriangleArea(7, 5)
ta.printTriangleAreaInfo()
triangleArea = ta.getArea()
print(f'TriangleArea: {triangleArea}')


