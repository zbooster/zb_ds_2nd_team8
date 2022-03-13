for i in range(1, 101):
    numTen = i // 10
    numOne = i % 10
    if numTen == 0:
        print(f'[{i}]: 홀수!') if numOne % 2 == 1 else print(f'[{i}]: 짝수!')
    else:
        if numTen % 2 == 1:
            strTen = '홀수!!'
        else:
            strTen = '짝수!!'
        if numOne == 0:
            strOne = '0'
        elif numOne % 2 == 1:
            strOne = '홀수!!'
        else:
            strOne = '짝수!!'

        print(f'[{i}] 십의자리: {strTen}, 일의자리: {strOne}')

