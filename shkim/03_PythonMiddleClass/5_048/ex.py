import lotto as lt

selectNum = []
for i in range(6):
    num = int(input('번호(1~45) 입력: '))
    selectNum.append(num)

lt.runLotto(selectNum)
