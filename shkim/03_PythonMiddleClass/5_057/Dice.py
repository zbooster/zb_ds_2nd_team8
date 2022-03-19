import random


class Dice:

    def __init__(self, maxNum=6):
        self.comNum = 0
        self.userNum = 0
        self.maxNum = maxNum

    def setCnum(self):
        print('[Dice] setCnum()')
        self.comNum = random.randint(1, 6)

    def setUnum(self):
        print('[Dice] setUnum()')
        self.userNum = random.randint(1, 6)

    def startGame(self):
        print('[Dice] startGame()')
        self.setCnum()
        self.setUnum()

    def printResult(self):
        print('[Dice] printResult()')
        result = '무승부!!'
        if self.comNum > self.userNum:
            result = '컴퓨터 승!!'
        elif self.comNum < self.userNum:
            result = '유저 승!!'
        print(f'컴퓨터 vs 유저 : {self.comNum} vs {self.userNum} >> {result}')
