cha1 = 'A'
cha2 = 'S'

print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))

print('\'A\' -> {}'.format(ord('A')))
print('\'a\' -> {}'.format(ord('a')))

print('65 -> {}'.format(chr(65)))
print('85 -> {}'.format(chr(85)))

str1 = 'Hello'
str2 = 'hello'

print('{} == {} : {}'.format(str1, str2, (str1==str2)))
print('{} != {} : {}'.format(str1, str2, (str1!=str2)))

userInputAlphabet = input('알파벳 입력 : ')
print('{} : {}'.format(userInputAlphabet, ord(userInputAlphabet)))

userInputASCII = int(input('아스키코드 입력 : '))
print('{} : {}'.format(userInputASCII, chr(userInputASCII)))