students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}

print('students[\'s1\']:{}'.format(students['s1']))
print('students[\'s2\']:{}'.format(students['s2']))
print('students[\'s3\']:{}'.format(students['s3']))
print('students[\'s4\']:{}'.format(students['s4']))
print('students[\'s5\']:{}'.format(students['s5']))

for key in students.keys():
    print('students[\'{}\']:{}'.format(key, students[key]))

print('students[\'s1\']:{}'.format(students.get('s1')))
# get() 함수는 Error를 발생 시키지 않는다.
print('students[\'s1\']:{}'.format(students.get('s6')))

myInfo = {'이름':'박경진',
          '전공':'computer',
          '메일':'jin@naver.com',
          '학년':3,
          '주소':'대한민국 서울',
          '취미':['요리', '여행']}

for key in myInfo.keys():
    print('myInfo[\'{}\']: {}'.format(key, myInfo[key]))

for key in myInfo.keys():
    print('myInfo.get(\'{}\'): {}'.format(key, myInfo.get(key)))