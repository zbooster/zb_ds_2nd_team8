# for i in range(1, 1+5):
#     print('*'*(i))
#
# for i in range(1, 1+5):
#     print(' '*(5-i) + '*'*i)
#
# for i in range(1, 1+5):
#     print('*'*(5-i) + ' '*i)
#
# for i in range(5):
#     print(' '*(i) + '*'*(5-i))
#
# for i in range(1, 1+5):
#     print('*'*(i))
# for i in range(5):
#     print('*'*(4-i) + ' '*i)
#
# for i in range(1, 1+5):
#     for j in range(1, 1+i):
#         if i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# for i in range(5, 0, -1):
#     for j in range(1, 1+i):
#         if i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

flag = True
n = 1
while n > 0:
    print(' ' * (5 - n), end='')
    print('*' * (2 * n - 1), end='')
    if n == 5 and flag:
        flag = False
    else:
        if flag:
            n += 1
        else:
            n -= 1
    print()

