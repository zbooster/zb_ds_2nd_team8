import random

nums = random.sample(range(50, 101), 20)
ranks = [0 for i in range(len(nums))]

print(f'nums: {nums}')
print(f'ranks: {ranks}')

for idx, num1 in enumerate(nums):
    for num2 in nums:
        if num1 < num2:
            ranks[idx] += 1

print(f'nums:  {nums}')
print(f'ranks: {ranks}')