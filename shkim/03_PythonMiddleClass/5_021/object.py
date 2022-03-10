class TmpCls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClsInfo(self):
        print(f'self.number: {self.number}')
        print(f'self.str: {self.str}')

# 앝은 복사
# tc1 = TmpCls(10, 'Hello')
# tc2 = tc1
#
# tc1.printClsInfo()
# tc2.printClsInfo()
#
# tc2.number = 3.14
# tc2.str = 'Bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()

# 깊은 복사
# import copy
# tc1 = TmpCls(10, 'Hello')
# tc2 = copy.copy(tc1)
#
# tc1.printClsInfo()
# tc2.printClsInfo()
#
# tc2.number = 3.14
# tc2.str = 'Bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()

scores = [9, 8, 5, 7, 6, 10]

scoresCopy = scores
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')

scoresCopy = []
for s in scores:
    scoresCopy.append(s)
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')

scoresCopy = []
scoresCopy.extend(scores)
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')

scoresCopy = scores.copy()
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')

scoresCopy = scores[:]
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')