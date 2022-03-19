import random
import sortMod as sm

scores = [ random.randint(50, 100) for i in range(20) ]
print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

sn = sm.sortNumber(scores)
sn.setSort()
print(f'result(ASC):  {sn.getSortedNum()}')
sn.isAscending(False)
sn.setSort()
print(f'result(DESC): {sn.getSortedNum()}')

