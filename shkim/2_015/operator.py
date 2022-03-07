# num1 = 10
# num2 = 3
#
# result = num1 / num2
# print(result)
#
# result = num1 // num2
# print(result)
#
# result = num1 % num2
# print(result)
#
# result = divmod(num1, num2)
# print('result: {}'.format(result))
# print('몫: {}'.format(result[0]))
# print('나머지: {}'.format(result[1]))

# allStuCnt = int(input('전체 학생 수 : '))
# stuCntOfGroup = int(input('한 모둠 학생 수 : '))
#
# print('전체 학생 수 : {}'.format(allStuCnt))
# print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
#
# result = divmod(allStuCnt, stuCntOfGroup)
#
# print('모둠 수 : {}'.format(result[0]))
# print('남는 학생 수 : {}'.format(result[1]))

appleCnt = 123
applePerEmployee = 4

result = divmod(appleCnt, applePerEmployee)

print('사과를 나누어 줄 수 잇는 최대 직원수 : {}명'.format(result[0]))
print('남는 사과 개수 : {}개'.format(result[1]))


