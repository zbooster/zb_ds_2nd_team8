# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
# print('students: {}'.format(students))
#
# students.sort(reverse=False)
# print('students: {}'.format(students))
#
# students.sort(reverse=True)
# print('students: {}'.format(students))

# numbers = [2, 30, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
# print('numbers: {}'.format(numbers))
#
# numbers.sort()
# print('numbers: {}'.format(numbers))

playerScores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print('playerScores: {}'.format(playerScores))

playerScores.sort()
print('playerScores: {}'.format(playerScores))

playerScores.pop(len(playerScores)-1)
playerScores.pop(0)
print('playerScores: {}'.format(playerScores))

total = sum(playerScores)
avg = total / len(playerScores)

print('총점: %.2f' % total)
print('평점: %.2f' % avg)