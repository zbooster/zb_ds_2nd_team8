selectNum = int(input('출퇴근 대상자 인가요? 1.Yes 2.No : '))

if selectNum == 1:
    print('교통수단을 선택하세요')
    trans = int(input('1.도보,자전거 2.버스,지하철 3.자가용'))

    if trans == 1:
        print('세금감면 5%')
    elif trans == 2:
        print('세금감면 3%')
    elif trans == 3:
        print('추가세금 1%')
    else:
        print('잘못 입력하셨습니다.')

elif selectNum == 2:
    print('세금변동 없음')
else:
    print('잘못 입력하셨습니다.')