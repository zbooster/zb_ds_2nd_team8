# speed = int(input('속도 입력: '))
#
# if speed > 50:
#     print('안전속도 위반!! 과태료 50,000원 부과 대상!!!')
# else:
#     print('안전속도 준수!!')

msg = input('메세지 입력: ')
lengthMsg = len(msg)

if lengthMsg <= 50:
    print('SMS 발송!!')
    print('메시지 길이: {}'.format(lengthMsg))
    print('메시지 발송 요금: 50원')
else:
    print('MMS 발송!!')
    print('메시지 길이: {}'.format(lengthMsg))
    print('메시지 발송 요금: 100원')