def calPermutation(n, r, isPrint=True):

    result = 1
    for i in range(n, n-r, -1):
        result *= i

    return result

def calCombination(n, r, isPrint=True):

    resultP = calPermutation(n, r)
    resultR = 1
    for i in range(r, 1, -1):
        resultR *= i
    resultC =int(resultP / resultR)
    if isPrint:
        print(f'resultP: {resultP}')
        print(f'resultR: {resultR}')
        print(f'resultC: {resultC}')
    return resultC


def printCombination(n, r, selNum=[]):
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
            if len(selNum) == 0 or i > max(selNum):
                selNum.append(i)
                printCombination(n, r - 1, selNum)
                selNum.remove(i)


if __name__ == '__main__':
    calCombination(8, 3)
    printCombination(8, 3)


