# memInfo = {'이름':'박경진',
#           '전공':'computer',
#           '메일':'jin@naver.com',
#           '학년':3,
#           '주소':'대한민국 서울',
#           '취미':['요리', '여행']}
#
# print('이름' in memInfo)
# print('메일' in memInfo)
# print('학년' in memInfo)
# print('취미' in memInfo)
#
# print('이름' not in memInfo)
# print('메일' not in memInfo)
# print('학년' not in memInfo)
# print('취미' not in memInfo)
#
# print(f'len(memInfo): {len(memInfo)}')
#
# print(f'memInfo: {memInfo}')
# memInfo.clear()
# print(f'memInfo: {memInfo}')

myInfo = {'이름':'박경진',
          '전공':'computer',
          '연락처':'010-0000-0000',
          '학년':3,
          '주민등록번호':'888888-8888888',
          '취미':['요리', '여행']}

print(f'myInfo: {myInfo}')

deleteItems = ['연락처', '주민등록번호']

for item in deleteItems:
    if (item in myInfo):
        del myInfo[item]

print(f'myInfo: {myInfo}')