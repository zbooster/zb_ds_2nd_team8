import datetime

dustNum = int(input('미세먼지 수치 입력: '))
carSector = int(input('1.승용차 2.영업용차 '))
carNumber = input('차량 번호 입력: ')
endCarNumber = int(carNumber[3])

lt = datetime.datetime.now()

print('-'*30)
print(lt)
print('-'*30)
if (dustNum > 150) and (carSector == 1):
    if (lt.day % 2) != (endCarNumber % 2):
        print('금일 운행 가능합니다.')
    else:
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량 입니다.')
else:
    if (lt.day % 5) != (endCarNumber % 5):
        print('금일 운행 가능합니다.')
    else:
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량 입니다.')

print('-'*30)