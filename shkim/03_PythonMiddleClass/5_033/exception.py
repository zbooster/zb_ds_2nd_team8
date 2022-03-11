# class NotUseZeroException(Exception):
#
#     def __init__(self, n):
#         super().__init__(f'{n}은 사용할 수 없습니다.')
#
#
# def divCalculator(n1, n2):
#
#     if n2 == 0:
#         raise NotUseZeroException(n2)
#     else:
#         print(f'{n1} / {n2} = {n1 / n2}')
#
#
# num1 = int(input('input number1: '))
# num2 = int(input('input number2: '))
#
# try:
#     divCalculator(num1, num2)
# except NotUseZeroException as e:
#     print(e)

class PasswordLengthShortException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 길이 5미만!!')


class PasswordLengthLongException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 길이 10초과!!')


class PasswordWrongException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 잘못된 비밀번호!!')


def checkPassword(str):
    if len(str) < 5:
        raise PasswordLengthShortException(str)
    elif len(str) > 10:
        raise  PasswordLengthLongException(str)
    elif str == 'admin1234':
        print('빙고!')
    else:
        raise PasswordWrongException(str)


inputPassword = input('input admin password: ')
checkPassword(inputPassword)
