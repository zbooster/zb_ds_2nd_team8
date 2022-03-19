nums = [10, 2, 7, 21, 0]
print(f'nums: {nums}')
print()

length = len(nums) - 1
for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j+1]:
            # tmp = nums[j]
            # nums[j] = nums[j+1]
            # nums[j+1] = tmp
            nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
    print()

print(f'sorted nums: {nums}')
