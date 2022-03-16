# memInfo = {'이름':'박경진',
#           '전공':'computer',
#           '메일':'jin@naver.com',
#           '학년':3,
#           '주소':'대한민국 서울',
#           '취미':['요리', '여행']}
#
# print(f'memInfo: {memInfo}')
#
# del memInfo['메일']
# print(f'memInfo: {memInfo}')
#
# del memInfo['취미']
# print(f'memInfo: {memInfo}')
#
# memInfo = {'이름':'박경진',
#           '전공':'computer',
#           '메일':'jin@naver.com',
#           '학년':3,
#           '주소':'대한민국 서울',
#           '취미':['요리', '여행']}
#
# returnValue = memInfo.pop('메일')
# print(f'memInfo: {memInfo}')
# print(f'returnValue: {returnValue}')
# print(f'returnValue type: {type(returnValue)}')

scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score4':9.8, 'score5':8.8}
print(f'scores: {scores}')

minScore = 10; minScoreKey = ''
maxScore = 0; maxScoreKey = ''

for key in scores.keys():
    if scores[key] > maxScore:
        maxScore = scores[key]
        maxScoreKey = key

    if scores[key] < minScore:
        minScore = scores[key]
        minScoreKey = key

del scores[minScoreKey]
del scores[maxScoreKey]
print(f'scores: {scores}')