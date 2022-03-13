busA = [ i for i in range(60 * 6, 60 * 23 + 1, 15) ]
busB = [ i for i in range(60 * 6, 60 * 23 + 1, 13) ]
busC = [ i for i in range(60 * 6 + 20, 60 * 22 + 1, 8) ]

for i in range(60 * 6, 60 * 23 + 1):
    if busA.count(i) + busB.count(i) + busC.count(i) > 1:
        if busA.count(i) and busB.count(i) and busC.count(i):
            print('busA와 busB와 busC 동시 정차!! {}:{}'.format((i // 60), (i % 60)))
        elif busA.count(i) and busB.count(i):
            print('busA와 busB 동시 정차!! {}:{}'.format((i//60), (i%60)))
        elif busA.count(i) and busC.count(i):
            print('busA와 busC 동시 정차!! {}:{}'.format((i//60), (i%60)))
        elif busB.count(i) and busC.count(i):
            print('busB와 busC 동시 정차!! {}:{}'.format((i//60), (i%60)))
