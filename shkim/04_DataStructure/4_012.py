# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# rValue = students.pop()
# print('rValue: {}'.format(rValue))
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# students.pop(3)
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))

scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]

maxIdx = 0
minIdx = 0

for idx, score in enumerate(scores):
    if score == max(scores):
        maxIdx = idx
    if score == min(scores):
        minIdx = idx

print('playerScore: {}'.format(scores))
for idx, score in enumerate(scores):
    if score == min(scores):
        minIdx = idx
print('minScore: {}, minScoreIdx: {}'.format(min(scores), minIdx))
scores.pop(minIdx)
print('playerScore: {}'.format(scores))

for idx, score in enumerate(scores):
    if score == max(scores):
        maxIdx = idx
print('maxScore: {}, maxScoreIdx: {}'.format(max(scores), maxIdx))
scores.pop(maxIdx)
print('playerScore: {}'.format(scores))