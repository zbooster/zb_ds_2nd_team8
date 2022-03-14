# sports = ['농구', '수구', '축구', '마라톤', '테니스']
#
# favoriteSport = input('가장 좋아하는 스포츠 입력: ')
#
# bestSportIdx = 0
# for idx, name in enumerate(sports):
#     if name == favoriteSport:
#         bestSportIdx = idx + 1
#
# print('{}(은)는 {}번째에 있습니다.'.format(favoriteSport, bestSportIdx))

msg = input('메세지 입력: ')
emptyCnt = 0
for idx, char in enumerate(msg):
    if char == ' ':
        emptyCnt += 1

print('공백 개수: {}'.format(emptyCnt))