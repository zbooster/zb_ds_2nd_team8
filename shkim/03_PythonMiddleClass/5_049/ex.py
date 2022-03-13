import permutation as pt

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

numP = pt.calPermutation(numN, numR)
print('{}P{} 개수: {}'.format(numN,numR,numP))

pt.printPermutation(numN, numR)

