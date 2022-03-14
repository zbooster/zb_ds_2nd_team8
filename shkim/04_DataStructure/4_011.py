# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철']
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# students.insert(3, '강호동')
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))

# words = ['I', 'a', 'boy']
# words.insert(1, 'am')
#
# for word in words:
#     print(word, end=' ')

numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputNumber = int(input('숫자 입력: '))
insertIdx = 0

for idx, num in enumerate(numbers):
    if inputNumber < num:
        insertIdx = idx
        break

numbers.insert(insertIdx, inputNumber)
print('numbers: {}'.format(numbers))
