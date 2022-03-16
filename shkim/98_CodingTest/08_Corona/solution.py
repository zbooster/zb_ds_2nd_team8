def solution(history, infected):
    area = []
    areaHis = []

    for num in history:
        if num > 0:
            area.append(num)
        else:
            area.remove((num * -1))
        areaHis.append(area.copy())

    print(areaHis)

    infectedList = []
    for arr in areaHis:
        if infected in arr:
            infectedList += arr

    print(infectedList)

    result = []
    for num in infectedList:
        if (num != infected) and (num not in result):
            result.append(num)

    result.sort()

    return result


if __name__ == '__main__':
    history = [3, 2, -3, 1, -1, -2, 4, -4, 1, -1]
    solution(history, 2)