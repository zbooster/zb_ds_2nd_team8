# scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
# print('scores: {}'.format(scores))
#
# minScore = 60
# fStr = 'F(재시험)'
# if scores['kor'] < minScore: scores['kor'] = fStr
# if scores['eng'] < minScore: scores['eng'] = fStr
# if scores['mat'] < minScore: scores['mat'] = fStr
# if scores['sci'] < minScore: scores['sci'] = fStr
# if scores['his'] < minScore: scores['his'] = fStr
# print('scores: {}'.format(scores))


myBodyInfo = {'이름':'gildong', '몸무게':83.0, '신장':1.8}
myBMI = myBodyInfo['몸무게'] / myBodyInfo['신장'] ** 2
print(f'myBodyInfo: {myBodyInfo}')
print(f'myBMI: {round(myBMI, 2)}')

for i in range(30):
    myBodyInfo['몸무게'] -= 0.3
    myBodyInfo['신장'] += 0.001

myBMI = myBodyInfo['몸무게'] / myBodyInfo['신장'] ** 2
print(f'myBodyInfo: {myBodyInfo}')
print(f'myBMI: {round(myBMI, 2)}')