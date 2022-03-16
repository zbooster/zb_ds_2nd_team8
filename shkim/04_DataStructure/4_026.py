# students = ['홍길동', '박찬호', '이용규', '강호동']
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))
#
# students = ('홍길동', '박찬호', '이용규', '강호동')
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))
#
# students = '홍길동', '박찬호', '이용규', '강호동'
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))
#
# students = ['홍길동', '박찬호', '이용규', '강호동']
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))
#
# students = tuple(students)
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))
#
# students = list(students)
# print('students: {}'.format(students))
# print('students: {}'.format(type(students)))

playerScores = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('playerScores: {}'.format(playerScores))
print('playerScores: {}'.format(type(playerScores)))

playerScores = list(playerScores)
print('playerScores: {}'.format(type(playerScores)))

playerScores.sort()
print('playerScores: {}'.format(playerScores))

playerScores.pop(len(playerScores)-1)
playerScores.pop(0)

playerScores = tuple(playerScores)
print('playerScores: {}'.format(playerScores))
print('playerScores: {}'.format(type(playerScores)))

total = sum(playerScores)
avg = total / len(playerScores)

print('총점: %.2f' % total)
print('평점: %.2f' % avg)