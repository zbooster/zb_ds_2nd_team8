# weight = input('체중 입력(g): ')
# height = input('신장 입력(cm): ')
#
# if weight.isdigit():
#     weightNum = float(weight) / 10
#     print('체중: %.1fkg' % (weightNum))
#
# if height.isdigit():
#     heightNum = float(height) / 100
#     print('신장: %.2fm' % (heightNum))
#
# print('BMI : %.2f' % (weightNum / (heightNum * heightNum)))

# num1 = 10
# num2 = 20
# print('num1: {}, num2: {}'.format(num1, num2))
# print('num1: {1}, num2: {0}'.format(num1, num2))

midScore = input('중간 고사 점수: ')
endScore = input('기말 고사 점수: ')

if midScore.isdigit() and endScore.isdigit():
    midScore = int(midScore)
    endScore = int(endScore)
    total = midScore + endScore
    avg = total / 2
    print('총점: %d, 평균: %.1f' % (total, avg))
else:
    print('잘 못 입력했습니다.')