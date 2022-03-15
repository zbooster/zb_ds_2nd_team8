# students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
#
# for i in range(5):
#     print('students[{}]: {}'.format(i, students[i]))


students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

for i in range(5):
    if i % 2 == 0:
        print('짝수 인덱스: students[{}]: {}'.format(i, students[i]))
    else:
        print('홀수 인덱스: students[{}]: {}'.format(i, students[i]))