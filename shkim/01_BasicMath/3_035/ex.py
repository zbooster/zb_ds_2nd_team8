# dNum = int(input('10진수 입력: '))
#
# print('2진수: {}'.format(bin(dNum)))
# print('8진수: {}'.format(oct(dNum)))
# print('16진수: {}'.format(hex(dNum)))
#
# print('2진수(0b10101) -> 10진수({})'.format(int('0b10101', 2)))
# print('8진수(0o135) -> 10진수({})'.format(int('0o135', 8)))
# print('16진수(0x5f) -> 10진수({})'.format(int('0x5f', 16)))

print('2진수(0b10101) -> 8진수({})'.format(oct(0b10101)))
print('2진수(0b10101) -> 10진수({})'.format(int(0b10101)))
print('2진수(0b10101) -> 16진수({})'.format(hex(0b10101)))

print('8진수(0o675) -> 2진수({})'.format(bin(0o675)))
print('8진수(0o675) -> 10진수({})'.format(int(0o675)))
print('8진수(0o675) -> 16진수({})'.format(hex(0o675)))

print('16진수(0x45d) -> 2진수({})'.format(bin(0x45d)))
print('16진수(0x45d) -> 8진수({})'.format(oct(0x45d)))
print('16진수(0x45d) -> 10진수({})'.format(int(0x45d)))