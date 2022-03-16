# myInfo = {}
#
# myInfo['이름'] = '박경진'
# myInfo['전공'] = 'computer'
# myInfo['메일'] = 'jin@gmail.com'
# myInfo['학년'] = 3
# myInfo['주소'] = 'korea seoul'
# myInfo['취미'] = ['수영', '여행']
#
# print(myInfo)
#
# myInfo['메일'] = 'jin@naver.com'
#
# print(myInfo)

# students = {}
#
# students['name'] = input('이름 입력: ')
# students['grade'] = input('학년 입력: ')
# students['mail'] = input('메일 입력: ')
# students['addr'] = input('주소 입력: ')
#
# print(f'students: {students}')

factorialDic = {}
for i in range(11):
    if i == 0:
        factorialDic[i] = 1
    else:
        for j in range(1, (1+i)):
            factorialDic[i] = factorialDic[i-1] * j

print(f'factorialDic: {factorialDic}')