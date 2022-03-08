# cnt = 0
#
# for i in range(1, 100):
#     if i % 7 != 0:
#         continue
#     print('{}는 7의 배수입니다.'.format(i))
#     cnt += 1
# else:
#     print('99까지의 정수 중 7의 배수는 {}개 입니다.'.format(cnt))
#

minNum = 0
for i in range(1, 100):
    if (i % 3 != 0) or (i % 7 !=0):
        continue
    print('{}는 3과 7의 공배수 입니다.'.format(i))

    if minNum == 0:
        minNum = i
else:
    print('3과 7의 최소공배수는 {} 입니다.'.format(minNum))


