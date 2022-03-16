# myInfo = {'이름':'박경진',
#           '전공':'computer',
#           '메일':'jin@naver.com',
#           '학년':3,
#           '주소':'대한민국 서울',
#           '취미':['요리', '여행']}
#
# ks = myInfo.keys()
# print('ks: {}'.format(ks))
# print('ks\'s type: {}'.format(type(ks)))
#
# vs = myInfo.values()
# print('ks: {}'.format(vs))
# print('ks\'s type: {}'.format(type(vs)))
#
# items = myInfo.items()
# print('ks: {}'.format(items))
# print('ks\'s type: {}'.format(type(items)))
#
scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print('scores: {}'.format(scores))

minScore = 60
fStr = 'F(재시험)'
for key in scores:
    if scores[key] < minScore: scores[key] = fStr

print('scores: {}'.format(scores))