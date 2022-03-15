# students1 = ('홍길동', '박찬호', '이용규')
# students2 = ('박승철', '김지은', '강호동')
# print('students1: {}'.format(students1))
# print('students2: {}'.format(students2))
#
# students3 = students1 + students2
# print('students3: {}'.format(students3))

myNumbers = (1, 3, 5, 6, 7)
friendNumbers = (2, 3, 5, 8, 10)

print('myNumbers: {}'.format(myNumbers))
print('friendNumbers: {}'.format(friendNumbers))

for num in friendNumbers:
    if num not in myNumbers:
        myNumbers += (num, )

print('myNumbers: {}'.format(myNumbers))