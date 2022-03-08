inputNum = int(input('희망 구구단 입력 : '))

n = 1
while n <= 9:
    print('{} x {} = {}'.format(inputNum, n, (inputNum*n)))
    n += 1