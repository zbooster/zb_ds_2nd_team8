import discount as ds

orderList = []

while True:
    selNum = int(input('상품을 구매 하시겠어요? 1.구매 2.종료 '))
    if selNum == 1 :
        price = int(input('상품 가격 입력: '))
        orderList.append(price)
    elif selNum == 2 :
        break

disRate = (1 - ds.calDiscount(orderList)/100)
total = round(sum(orderList) * disRate)
print('합계: {}원'.format(format(total, ',')))


