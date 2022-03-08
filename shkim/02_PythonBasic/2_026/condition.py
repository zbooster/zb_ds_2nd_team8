# 계절을 입력하면 영어로 번역되는 프로그램을 만들어 보자.
# print('계절 : 봄, 여름, 가을, 겨울')
# seasonStr = input('계절 입력 : ')
#
# if seasonStr == '봄':
#     print('{} : {}'.format(seasonStr, 'spring'))
# elif seasonStr == '여름':
#     print('{} : {}'.format(seasonStr, 'summer'))
# elif seasonStr == '가을':
#     print('{} : {}'.format(seasonStr, 'fall'))
# elif seasonStr == '겨울':
#     print('{} : {}'.format(seasonStr, 'winter'))
# else:
#     print('검색할 수 없습니다.')

print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5.밀크티(4.3)')
menuNum = int(input('메뉴 선택 : '))

print('-'*30)
if menuNum == 1:
    print('메뉴 : 카페라떼\n가격 : 3,500원')
elif menuNum == 2:
    print('메뉴 : 에스프레소\n가격 : 3,000원')
elif menuNum == 3:
    print('메뉴 : 아메리카노\n가격 : 2,000원')
elif menuNum == 4:
    print('메뉴 : 곡물라떼\n가격 : 4,000원')
elif menuNum == 5:
    print('메뉴 : 밀크티\n가격 : 4,300원')
else:
    print('잘못 입력하셨습니다.')
print('-'*30)