# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
# print('students: {}'.format(students))
#
# students.reverse()
# print('students: {}'.format(students))

secret = '27156231'
secretList = []
solvedList = ''

for num in secret:
    secretList.append(int(num))

secretList.reverse()
print(f'secretList: {secretList}')

val = secretList[0] + secretList[1]
secretList.insert(2, val)

val = secretList[3] + secretList[4]
secretList.insert(5, val)

val = secretList[6] + secretList[7]
secretList.insert(8, val)

val = secretList[9] + secretList[10]
secretList.insert(11, val)

print(f'secretList: {secretList}')

