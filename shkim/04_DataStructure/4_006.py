# minScore = 60
#
# scores = [['국어', 58],
#           ['영어', 77],
#           ['수학', 89],
#           ['과학', 99],
#           ['국사', 50]]
#
# for item in scores:
#     if item[1] < minScore:
#         print('과락 과목: {}, 점수: {}'.format(item[0], item[1]))
#
# for subject, score in scores:
#     if score < minScore:
#         print('과락 과목: {}, 점수: {}'.format(subject, score))
#
# for subject, score in scores:
#     if score >= minScore: continue
#     print('과락 과목: {}, 점수: {}'.format(subject, score))

# minScore = 60
#
# korScore = int(input('국어 점수: '))
# engScore = int(input('영어 점수: '))
# matScore = int(input('수학 점수: '))
# sciScore = int(input('과학 점수: '))
# hisScore = int(input('국사 점수: '))
#
# scores = [
#     ['국어', korScore],
#     ['영어', engScore],
#     ['수학', matScore],
#     ['과학', sciScore],
#     ['국사', hisScore]]
#
# for subject, score in scores:
#     if score < minScore:
#         print('과락 과목: {}, 점수: {}'.format(subject, score))

studuntCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

minClass = []
maxClass = []

for i in range(len(studuntCnts)):
    if i == 0:
        minClass = studuntCnts[i]
        maxClass = studuntCnts[i]
    else:
        if minClass[1] > studuntCnts[i][1]:
            minClass = studuntCnts[i]
        if maxClass[1] < studuntCnts[i][1]:
            maxClass = studuntCnts[i]

print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minClass[0], minClass[1]))
print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxClass[0], maxClass[1]))

