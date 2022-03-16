def solution(area):
    resolusions = []

    for i in range(1, int(area ** (1/2))+1):
        if area % i == 0:
            #if i < int((area/i)):
            resolusions.append([i, int((area/i))])

    print(resolusions)
    return resolusions.pop()


if __name__ == '__main__':
    solution(16)


