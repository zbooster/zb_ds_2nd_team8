# nums = []
#
# while len(nums) < 5:
#
#     try:
#         n = int(input('input number: '))
#
#     except:
#         print('숫자가 입력되지 않았습니다.')
#         continue
#
#     if n % 2 == 0:
#         nums.append(n)
#     else:
#         print('홀수 입니다. 다시 입력하세요.')
#
# print(f'nums: {nums}')

evenList = []
oddList = []
floatList = []

n = 0

while n < 5:
    try:
        inputNum = float(input('숫자를 입력하세요: '))
    except:
        print('숫자가 입력되지 않았습니다.')
        continue
    else:
        if inputNum % 1 != 0:
            floatList.append(inputNum)
        elif inputNum % 2 == 0:
            oddList.append(int(inputNum))
        else:
            evenList.append(int(inputNum))
        n += 1

print(f'evenList: {evenList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')




