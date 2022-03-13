def calDiscount(orders):
    discountRate = 0
    if len(orders) >= 5:
        discountRate = 25
    else:
        discountRate = len(orders) * 5

    print('할인율: {}'.format(discountRate))
    return discountRate