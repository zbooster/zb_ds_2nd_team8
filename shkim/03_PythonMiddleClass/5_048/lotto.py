import random

def runLotto(selectNum):

    def genrateLotto():
        lottoNum = []
        while len(lottoNum) < 7:
            num = random.randint(1, 45)
            if lottoNum.count(num) == 0:
                lottoNum.append(num)

        return lottoNum

    def checkNumber(selectNum, lottoNum):
        matchList = []
        for sn in selectNum:
            if lottoNum.count(sn) > 0:
                matchList.append(sn)

        return matchList

    def printResult():
        if len(matchList) > 2:
            print('축하합니다.')
        else:
            print('아쉽습니다. 다음 기회에~')

        print('기계번호: {}'.format(lottoNum))
        print('보너스 번호: {}'.format(bonusNum))
        print('선택번호: {}'.format(selectNum))
        print('일치번호: {}'.format(matchList))

    lottoNum = genrateLotto()
    matchList = checkNumber(selectNum, lottoNum)
    bonusNum = lottoNum.pop(6)
    printResult()


if __name__ == '__main__':
    runLotto([5, 15, 25, 30, 45, 9])
