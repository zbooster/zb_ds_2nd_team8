# for i in range(1, 10):
#     for j in range(i):
#         print('*', end='')
#     print()

# for i in range(10, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

for i in range(1, 10):
    for j in range(2, 10):
        print('{} x {} = {}\t'.format(j, i, (j*i)), end='')
    print()