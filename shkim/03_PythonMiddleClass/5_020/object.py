# class Robot:
#
#     def __init__(self, color, height, weight):
#         self.color = color
#         self.height = height
#         self.weigth = weight
#
#     def printRobotInfo(self):
#         print(f'color: {self.color}')
#         print(f'height: {self.height}')
#         print(f'weigth: {self.weigth}')
#
# rb1 = Robot('red', 200, 80)
# rb2 = Robot('blue', 300, 120)
# rb3 = rb1
#
# rb1.printRobotInfo()
# rb2.printRobotInfo()
# rb3.printRobotInfo()
#
# rb1.color = 'gray'
# rb1.height = 250
# rb1.weigth = 100
# rb1.printRobotInfo()
# rb2.printRobotInfo()
# rb3.printRobotInfo()


scores = [int(input('국어 점수 입력: ')),
          int(input('영어 점수 입력: ')),
          int(input('수학 점수 입력: '))]

print(scores)

copyScores = scores.copy()

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'이전 평균: {sum(scores)/len(scores)}')
print(f'이후 평균: {sum(copyScores)/len(copyScores)}')