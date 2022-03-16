def solution(lineUp, level):
    # privPos = -1
    # for idx, val in enumerate(lineUp):
    #     if val == 1:
    #         if privPos < 0:
    #             privPos = idx
    #         elif (idx - privPos - 1) < level:
    #             return False
    #         else:
    #             privPos = idx

    cnt = 0
    startIdx = lineUp.index(1)
    for val in lineUp[startIdx + 1:]:
        if val == 0:
            cnt += 1
        else:
            if cnt < level:
                return False
            cnt = 0

    # position = []
    # for idx, val in enumerate(lineUp):
    #     if val == 1:
    #         position.append(idx)
    #
    # for i in range(len(position)):
    #     if i != 0:
    #         dist = position[i] - position[i-1] - 1
    #         if dist < level:
    #             return False

    return True


if __name__ == '__main__':
    print(solution([0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0], 2))