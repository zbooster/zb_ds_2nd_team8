def divisor(n):
    returnList = []
    for i in range(1, n+1):
        if n % i == 0:
            returnList.append(i)

    return returnList

def prime_number(n):
    returnList = []
    for i in range(2, n+1):
        if len(divisor(i)) == 2:
            returnList.append(i)

    return returnList


if __name__ == '__main__':
    print(f'divisor(10): {divisor(10)}')
    print(f'prime_number(50): {prime_number(50)}')