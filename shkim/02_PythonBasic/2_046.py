korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

total = korScore + engScore + matScore
avg = total / 3

print('총점: {}'.format(total))
print('평균: %.2f' % avg)

print('-'*30)
#최고 점수 과목 구하기
if korScore > engScore:
    if korScore > matScore:
        maxSubject = '국어'
        maxScore = korScore
    else:
        maxSubject = '수학'
        maxScore = matScore
else:
    if engScore > matScore:
        maxSubject = '영어'
        maxScore = engScore
    else:
        maxSubject = '수학'
        maxScore = matScore

# 최저 점수 과목 구하기
if korScore < engScore:
    if korScore < matScore:
        minSubject = '국어'
        minScore = korScore
    else:
        minSubject = '수학'
        minScore = matScore
else:
    if engScore < matScore:
        minSubject = '영어'
        minScore = engScore
    else:
        minSubject = '수학'
        minScore = matScore

print(f'최고 점수 과목(점수): {maxSubject}({maxScore})')
print(f'최저 점수 과목(점수): {minSubject}({minScore})')
print(f'최고, 최저 점수 차이: {maxScore - minScore}')





print('-'*30)

