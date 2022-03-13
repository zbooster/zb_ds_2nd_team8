productPrice = int(input('상품 가격 입력: '))
payedAmount = int(input('지불 금액: '))

returnAmount = (payedAmount - productPrice)
returnAmount -= (returnAmount % 10)

print('거스름 돈: {}(원단위 절사)'.format(returnAmount))
print('-'*40)

for money in [50000, 10000, 5000, 1000, 500, 100, 10]:
    moneyNum = returnAmount // money
    if money > 500:
        print('{} {}장'.format(money, moneyNum))
    else:
        print('{} {}개'.format(money, moneyNum))
    returnAmount -= (money * moneyNum)

print('-'*40)