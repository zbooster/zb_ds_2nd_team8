import checkScore as cs


if __name__ == '__main__':
    inputScores = []
    for i in range(5):
        score = int(input('과목{} 점수 입력: '.format(i+1)))
        inputScores.append(score)

    r1 = cs.checkSubject(inputScores)
    r2 = cs.checkAverage(inputScores)
    if r1 and r2:
        print('Final Pass!!')
    else:
        print('Final Fail!!')

