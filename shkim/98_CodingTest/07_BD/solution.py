def solution(n):
    strBin = str(bin(n))[2:]

    dists = []
    dist = 1
    for c in strBin:
        if c == '0':
            dist += 1
            dists.append(dist)
        else:
            dist = 1

    return max(dists)


if __name__ == '__main__':
    n = 500

    # print(bin(11))
    # print(str(bin(11))[2:])

    strBin = str(bin(n))[2:]

    dists = []
    dist = 1
    for c in strBin:
        if c == '0':
            dist += 1
            dists.append(dist)
        else:
            dist = 1

    print(strBin)
    print(dists)
    print(max(dists))
