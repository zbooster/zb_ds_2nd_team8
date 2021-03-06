def calPermutation(n, r, isPrint=True):

    result = 1
    for i in range(n, n-r, -1):
        result *= i
        if isPrint:
            print('n : {}'.format(i))

    print('{}P{}: {}' .format(n, r, result))
    return result

def printPermutation(n, r, selNum=[]):
    if r == 0:
        lenList = len(selNum)
        for i in range(lenList):
            if i == 0:
                print('({},'.format(selNum[i]), end='')

            elif i == (lenList - 1):
                print(' {}), '.format(selNum[i]), end='')

            else:
                print(' {},'.format(selNum[i]), end='')

    else:
        for i in range(1, 1+n):
            if selNum.count(i) == 0:
                selNum.append(i)
                printPermutation(n, r - 1, selNum)
                selNum.remove(i)



if __name__ == '__main__':
    calPermutation(8, 3)
    printPermutation(8, 3)

