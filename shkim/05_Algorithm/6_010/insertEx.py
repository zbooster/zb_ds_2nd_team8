import random
import sortMod as sm

nums = random.sample(range(1, 1000), 100)
print(f'not sorted numbers: {nums}')

sn = sm.sortNumbers(nums)

# 오름차순
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers: {sortedNumbers}')

# 내림차순
sn.isAscending(False)
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers: {sortedNumbers}')

# min & max
print(f'min: {sn.getMinNumber()}')
print(f'max: {sn.getMaxNumber()}')

