import scores as sc

kor = int(input('국어 점수 입력: '))
eng = int(input('영어 점수 입력: '))
mat = int(input('수학 점수 입력: '))

sc.addScore(kor)
sc.addScore(eng)
sc.addScore(mat)

print(sc.getScores())
print(sc.getTotalScore())
print(sc.getAvgScore())