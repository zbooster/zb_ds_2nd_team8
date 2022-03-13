n1 = int(input('GearA 톱니수 입력: '))
n2 = int(input('GearB 톱니수 입력: '))

n1Tol = n1
n2Tol = n2

while True:
    print('gearA: {}, grarB: {}'.format(n1Tol, n2Tol))
    if n2Tol == n1Tol:
        break

    if n2Tol - n1Tol < n1:
        n2Tol += n2
    n1Tol += n1


print('최초 만나는 톱니수(최소공배수): {}톱니'.format(n2Tol))
print('gearA 회전수 : {}회전'.format(int(n2Tol/n1)))
print('gearB 회전수 : {}회전'.format(int(n2Tol/n2)))