def solution(s):
    splitInt = []
    strIdx = 0
    for idx, c in enumerate(s):
        if idx != 0 and (c == '-' or c == '+'):
            splitInt.append(int(s[strIdx:idx]))
            strIdx = idx

    splitInt.append(int(s[strIdx:]))

    return sum(splitInt)

if __name__ == '__main__':
    s = '-3+26-7'
    print(s)

    for i, c in enumerate(s):
        print('{} : {}'.format(i, c))

    print(s[0:2])
    print(s[2:5])
    print(s[5:])

    sl = [int(s[0:2]), int(s[2:5]), int(s[5:])]

    print(sl)
    print(sum(sl))

