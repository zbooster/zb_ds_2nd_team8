scores = []

def addScore(s):
    scores.append(s)

def getScores():
    return scores

def getTotalScore():
    return sum(scores)

def getAvgScore():
    return sum(scores)/len(scores)