# print('{} and {} : {}'.format(True, True, (True and True)))
# print('{} and {} : {}'.format(True, False, (True and False)))
# print('{} and {} : {}'.format(False, True, (False and True)))
# print('{} and {} : {}'.format(False, False, (False and False)))
#
# print('{} or {} : {}'.format(True, True, (True or True)))
# print('{} or {} : {}'.format(True, False, (True or False)))
# print('{} or {} : {}'.format(False, True, (False or True)))
# print('{} or {} : {}'.format(False, False, (False or False)))
#
# print('not {} : {}'.format(True, (not True)))
# print('not {} : {}'.format(False, (not False)))

# age = int(input('나이 입력 : '))
# print('age: {}, result: {}'.format(age, (age < 20 or age >= 65)))

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

avg = (kor + eng + mat) / 3
avgPass = avg >= 70
korPass = kor >= 60
engPass = eng >= 60
matPass = mat >= 60
print('평균: {}, 결과: {}'.format(avg, avgPass))
print('국어: {}, 결과: {}'.format(kor, korPass))
print('영어: {}, 결과: {}'.format(eng, engPass))
print('수학: {}, 결과: {}'.format(mat, matPass))
print('과락 결과: {}'.format((korPass and engPass and matPass)))
print('최종 결과: {}'.format((korPass and engPass and matPass and avgPass)))




