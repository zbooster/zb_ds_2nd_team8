def calFee(sub, normalNum, discountNum, price):
    normalTol = normalNum * price
    discountTol = int(discountNum * price * 0.5)
    print('{} {}명 요금: {}원'.format(sub, normalNum, format(normalTol, ',')))
    print('{} 할인 대상 {}명 요금: {}원'.format(sub, discountNum, format(discountTol,',')))

    return normalTol + discountTol


nums = []
discount = []
subs = ['유아', '소아', '성인']
prices = [18000, 25000, 50000]

for sub in subs:
    n = int(input(sub + ' 입력: '))
    d = int(input('할인대상 ' + sub + ' 입력: '))
    nums.append(n)
    discount.append(d)

print('=' * 40)
totalNum = 0
totalPirce = 0
for i in range(3):
    totalNum += (nums[i] + discount[i])
    totalPirce += calFee(subs[i], nums[i], discount[i], prices[i])
print('=' * 40)
print('Total: {}명'.format(totalNum))
print('TotalPrice : {}원'.format(format(totalPirce, ',')))
print('=' * 40)


