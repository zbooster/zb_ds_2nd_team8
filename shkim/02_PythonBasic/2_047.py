# hou = int(input('시간 입력: '))
# min = int(input('분 입력: '))
# sec = int(input('초 입력: '))
#
# print('{}초'.format(format(hou * 3600 + min * 60 + sec, ',')))

amount = int(input('금액 입력: '))
interest = float(input('이율 입력: '))
period = int(input('기간 입력: '))

print('-'*30)
print('이율: {}%'.format(interest))
print('원금: {}원'.format(format(amount, ',')))
# result = amount
# for i in range(period):
#     result += result * (interest / 100)

result = amount * ((1 + (interest/100)) ** period)
print('{}년 후 금액: {}원'.format(period, format(round(result), ',')))
print('-'*30)
