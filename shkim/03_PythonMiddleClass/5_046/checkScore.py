def checkSubject(scores):
    returnFlag = True
    print('총점: {}'.format(sum(scores)))
    print('평균: {}'.format(sum(scores)/len(scores)))
    for score in scores:
        if score >= 40:
            print('{}: Pass'.format(score))
        else:
            print('{}: Fail'.format(score))
            returnFlag = False
    return returnFlag


def checkAverage(scores):
    total = sum(scores)
    avg = total / len(scores)
    print('총점: {}'.format(total))
    print('평균: {}'.format(avg))

    if avg >= 60:
        return True
    else:
        return False


if __name__ == '__main__':
    print(checkSubject([100, 35, 85, 45, 90]))
    print(checkAverage([100, 35, 85, 45, 90]))

