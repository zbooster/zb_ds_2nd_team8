import combination as ct

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

numC = ct.calCombination(numN, numR)
print('{}C{} 개수: {}'.format(numN,numR,numC))

ct.printCombination(numN, numR)

