# minScore = 60
#
# scores = [['국어', 58],
#           ['영어', 77],
#           ['수학', 89],
#           ['과학', 99],
#           ['국사', 50]]
#
# n = 0
# while n < len(scores):
#     if scores[n][1] < minScore:
#         print('과락 과목: {}, 점수: {}'.format(scores[n][0], format(scores[n][1])))
#     n += 1

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
# n = 0
# while n < len(scores):
#     if scores[n][1] < minScore:
#         print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))
#     n += 1

studuntCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

minClass = []
maxClass = []

n = 0
while n < len(studuntCnts):
    if n == 0:
        minClass = studuntCnts[n]
        maxClass = studuntCnts[n]
    else:
        if minClass[1] > studuntCnts[n][1]:
            minClass = studuntCnts[n]
        if maxClass[1] < studuntCnts[n][1]:
            maxClass = studuntCnts[n]
    n += 1

print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minClass[0], minClass[1]))
print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxClass[0], maxClass[1]))

