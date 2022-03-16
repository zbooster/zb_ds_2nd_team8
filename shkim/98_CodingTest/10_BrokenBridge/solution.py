def solution(l):
    maxAreaList = []

    for h in range(1, 1+max(l)):
        maxArea = 0
        for lenNamu in l:
            if lenNamu >= h:
                maxArea += h
                maxAreaList.append(maxArea)
            else:
                maxArea = 0

    return max(maxAreaList)