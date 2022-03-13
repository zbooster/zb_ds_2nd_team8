# def fac(n):
#     result = 0
#     if n == 1:
#         result = 1
#     else:
#         result = n * fac(n-1)
#     return result
#
# num = int(input('input number: '))
# print(format(fac(num), ','))

def calSampleInterest(deposit, period, interest):
    return deposit * (1 + (interest/100) * period)

def calMonthCompoundInterest(deposit, period, interest):
    return deposit * ((1 + (interest/100) / 12) ** (period * 12))

def printYeild(deposit, period, interest, isSimple):
    typeOfInterest = ''; result = 0
    if isSimple:
        typeOfInterest = '단리'
        result = calSampleInterest(deposit, period, interest)
    else:
        typeOfInterest = '월복리'
        result = calMonthCompoundInterest(deposit, period, interest)

    print('[{} 계산기]'.format(typeOfInterest))
    print('=' * 40)
    print('예치금\t: {}원'.format(format(deposit, ',')))
    print('예치기간\t: {}년'.format(period))
    print('연 이율\t: {}%'.format(int(interest)))
    print('-' * 40)
    print('{}년 후 총 수령액: {}원'.format(period, format(round(result), ',')))
    print('=' * 40)


deposit = int(input('예치금(원): '))
period = int(input('기간(년): '))
interest = float(input('연 이율(%): '))

printYeild(deposit, period, interest, True)
printYeild(deposit, period, interest, False)