# students = ['홍길동', '박찬호', '이용규', '김지은', '박승철', '강호동']
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))
#
# students.remove('박찬호')
#
# print('students: {}'.format(students))
# print('students의 길이: {}'.format(len(students)))
# print('last index : {}'.format(len(students) - 1))

# students = ['홍길동', '박찬호', '이용규', '강호동', '김지은', '박승철', '강호동']
#
# while '강호동' in students:
#     print('students: {}'.format(students))
#     students.remove('강호동')
#
# print('students: {}'.format(students))

# myList = ['마케팅 회의', '회의록 정리', '점심 약속',
#           '월간 업무 보고', '치과 방문', '마트 장보기']
# print('일정: {}'.format(myList))
#
# removeItem = input('삭제 대상 입력: ')
# myList.remove(removeItem)
# print('일정: {}'.format(myList))

subjects = ['국어', '영어', '수학', '과학', '국사']
print('시험 과목표: {}'.format(subjects))
removeSub = input('삭제 과목명 입력: ')
while removeSub in subjects:
    subjects.remove(removeSub)
print('시험 과목표: {}'.format(subjects))