def reverse(str):
    returnValue = ''
    for i in range(len(str)-1, -1, -1):
        returnValue += str[i]
    return returnValue


