def solution(n, s, t):
    allStr = ('.' * n) + s + ('.' * n)
    t = t % (n + len(s))
    return allStr[t:t+n]


if __name__ == '__main__':
    n = 5
    s = 'Snowball'
    t = 20
    t = t % (n + len(s))
    allStr = ('.' * n) + s + ('.' * n)
    print(allStr)
    print(allStr[t:t+n])