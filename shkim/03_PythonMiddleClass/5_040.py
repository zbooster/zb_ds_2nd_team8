def addCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} + {num2} = {num1 + num2}')

def subCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} - {num2} = {num1 - num2}')

def mulCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} * {num2} = {num1 * num2}')

def divCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} / {num2} = {num1 / num2}')

def modCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} % {num2} = {num1 % num2}')

def floCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} // {num2} = {num1 // num2}')

def powCal():
    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('첫 번째 숫자 입력: '))
    print(f'{num1} ** {num2} = {num1 ** num2}')

while True:
    print('-'*100)
    selNum = int(input('1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5. 나머지, 6. 몫, 7. 제곱승, 8. 종료 '))

    if selNum == 1:
        addCal()
    elif selNum == 2:
        subCal()
    elif selNum == 3:
        mulCal()
    elif selNum == 4:
        divCal()
    elif selNum == 5:
        modCal()
    elif selNum == 6:
        floCal()
    elif selNum == 7:
        powCal()
    elif selNum == 8:
        print('Bye~')
        break

    print('-'*100)



