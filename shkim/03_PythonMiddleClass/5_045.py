def geometricSequence(a1, r, n):
    an = a1 * (r ** (n-1))
    sn = a1 * (1 - (r ** n)) / (1 - r)
    return [an, sn]


a1 = int(input('a1 입력: '))
r = int(input('공비 입력: '))
n = int(input('n 입력: '))

for i in range(1, 1+n):
    gs = geometricSequence(a1, r, i)
    print('{}번째 항의 값: {}'.format(i, gs[0]))
    print('{}번째 항까지의 합: {}'.format(i, int(gs[1])))