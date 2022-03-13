selectSector = int(input('업종선택(1.가정용\t 2.대중탕용\t 3.공업용): '))
usage = int(input('사용량 입력: '))

unitOfCharge = 0

if selectSector == 1:
    unitOfCharge = 540
elif selectSector == 2:
    if usage <= 50:
        unitOfCharge = 820
    elif (usage > 50) and (usage <= 300):
        unitOfCharge = 1920
    else:
        unitOfCharge = 2400
elif selectSector == 3:
    if usage <= 500:
        unitOfCharge = 240
    else:
        unitOfCharge = 470

print('='*30)
print('상수도 요금표')
print('-'*30)
print('사용량\t:\t요금')
print('{}\t:\t{}원'.format(usage, format(usage*unitOfCharge, ',')))
print('='*30)
