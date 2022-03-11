# n1 = 10; n2 = 0
#
# try:
#     print(n1 / n2)
# except:
#     print('예외가 발생했습니다.')
#
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)

nums = []

while len(nums) < 5:
    try:
        n = int(input('input number: '))
        nums.append(n)
    except:
        print('숫자가 입력되지 않았습니다.')

print(f'nums: {nums}')
