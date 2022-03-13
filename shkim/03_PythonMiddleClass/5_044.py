def toleranceSequence(a1, d, n):
    an = a1 + (n-1) * d
    sn = int(n * (a1 + an) / 2)
    return [an, sn]


a1 = int(input('a1 입력: '))
d = int(input('공차 입력: '))
n = int(input('n 입력: '))



for i in range(1, 1+n):
    ts = toleranceSequence(a1, d, i)
    print('{}번째 항의 값: {}'.format(i, ts[0]))
    print('{}번째 항까지의 합: {}'.format(i, ts[1]))