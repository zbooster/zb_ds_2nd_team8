# age = int(input('나의 입력: '))
#
# if (age <= 19) or (age >= 65):
#     endBirthYear = int(input('출생 연도 끝자리 입력: '))
#     if endBirthYear % 5 == 1:
#         print('월요일 접종 가능!!')
#     elif endBirthYear % 5 == 2:
#         print('화요일 접종 가능!!')
#     elif endBirthYear % 5 == 3:
#         print('수요일 접종 가능!!')
#     elif endBirthYear % 5 == 4:
#         print('목요일 접종 가능!!')
#     elif endBirthYear % 5 == 5:
#         print('금요일 접종 가능!!')
# else:
#     print('하반기 일정 확인하세요.')

byInch = 0.039

length = int(input('길이(mm) 입력: '))
print(f'{length}mm -> {round(length * byInch, 3)}inch')