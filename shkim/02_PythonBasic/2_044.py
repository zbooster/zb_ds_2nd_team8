# selectLanguage = int(input(
#     '언어 선택(Choose your language): 1.한국어 \t 2.English '))
#
# if selectLanguage == 1:
#     print('1. 샌드위치 \t 2. 햄버거 \t3. 쥬스 \t4. 커피 \t5. 아이스크림' )
# elif selectLanguage == 2:
#     print('1. Sandwich \t 2. Hamburger \t3. Juice \t4. Coffee \t5. Ice cream')

import time

age = input('나이 입력 : ')

if age.isdigit():
    age = int(age)
    lt = time.localtime()

    periodBak = 100 - age
    bakYear = lt.tm_year + periodBak - 1

    print('{}년({}년후)에 100살'.format(bakYear, periodBak))
else:
    print('잘 못 입력했습니다.')
