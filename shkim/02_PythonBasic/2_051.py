korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))
sicScore = int(input('과학 점수 입력: '))
hisScore = int(input('국사 점수 입력: '))

avgKor = 85;avgEng = 82;avgMat = 89;avgSic = 75;avgHis = 94
avgTotal = avgKor + avgEng + avgMat + avgSic + avgHis
avgClass = avgTotal / 5

devKor = korScore - avgKor
devEng = engScore - avgEng
devMat = matScore - avgMat
devSic = sicScore - avgSic
devHis = hisScore - avgHis

myTotal = korScore + engScore + matScore + sicScore + hisScore
devTotal = myTotal - avgTotal
myAvg = myTotal / 5
devAvg = round(myAvg - avgClass)

print('-'*65)
print(f'총점:{myTotal}({devTotal}), 평균: {myAvg}({devAvg})')
print(f'국어:{korScore}({devKor}), 영어:{engScore}({devEng}), '
      f'수학:{matScore}({devMat}), 과학:{sicScore}({devSic}), '
      f'국사:{hisScore}({devHis})')
print('-'*65)
graphLine = '+'*devKor if devKor >= 0 else '-'*(devKor*-1)
print('국어 편차: {}({})'.format(graphLine, devKor))
graphLine = '+'*devEng if devEng >= 0 else '-'*(devEng*-1)
print('영어 편차: {}({})'.format(graphLine, devEng))
graphLine = '+'*devMat if devMat >= 0 else '-'*(devMat*-1)
print('수학 편차: {}({})'.format(graphLine, devMat))
graphLine = '+'*devSic if devSic >= 0 else '-'*(devSic*-1)
print('과학 편차: {}({})'.format(graphLine, devSic))
graphLine = '+'*devHis if devHis >= 0 else '-'*(devHis*-1)
print('국사 편차: {}({})'.format(graphLine, devHis))
graphLine = '+'*devTotal if devTotal >= 0 else '-'*(devTotal*-1)
print('총점 편차: {}({})'.format(graphLine, devTotal))
graphLine = '+'*devAvg if devAvg >= 0 else '-'*(devAvg*-1)
print('평균 편차: {}({})'.format(graphLine, devAvg))
print('-'*65)