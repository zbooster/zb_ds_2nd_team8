def solution(city):
    busStation = []
    for hIdx, hVal in enumerate(city):
        for wIdx, wVal in enumerate(hVal):
            if wVal == 0:
                busStation.append([hIdx, wIdx])

    result = []
    for hIdx, hVal in enumerate(city):
        tmp = []
        for wIdx, wVal in enumerate(hVal):
            tmp.append(len(city)+len(hVal))
        result.append(tmp)

    for hBus, wBus in busStation:
        for hIdx, hVal in enumerate(city):
            for wIdx, wVal in enumerate(hVal):
                if result[hIdx][wIdx] > (abs(hIdx-hBus)+abs(wIdx-wBus)):
                    result[hIdx][wIdx] = abs(hIdx-hBus)+abs(wIdx-wBus)

    return result

if __name__ == '__main__':
    city = [[1,0,1],
            [1,1,1],
            [1,1,1]]

    dist = [[1, 0, 1],
            [2, 1, 2],
            [3, 2, 3]]

    dist = [[(0,0), (0,1), (0,2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)]
            ]

    dist_x = [[1, 0, 1],
              [1, 0, 1],
              [1, 0, 1]]

    dist_y = [[0, 0, 0],
              [1, 1, 1],
              [2, 2, 2]]

    busStop = [0, 1]
    for idxI, valI in enumerate(range(3)):
        for idxJ, valJ in enumerate(range(-1, 3)):
            # print('({}, {})'.format(abs(idxI-busStop[0]), abs(idxJ-busStop[1])), end=' ')
            # print('({}, {})'.format(idxI, idxJ), end=' ')
            print('({}, {})'.format(valI, valJ), end=' ')
        print()