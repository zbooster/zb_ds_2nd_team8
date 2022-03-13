# def getDistance(s, h, m):
#     return (h + m / 60) * s
#
#
# print('-' * 60)
# s = float(input('속도(km/h) 입력: '))
# h = float(input('시간(h) 입력: '))
# m = float(input('시간(h) 입력: '))
# d = getDistance(s, h, m)
# print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리: {d}(km)')
# print('-' * 60)

def getTime(s, d):
    resultList = []
    t = d / s
    resultList.append(int(t // 1))
    resultList.append(int((t % 1) * 60))
    return resultList

print('-' * 60)
s = float(input('속도(km/h) 입력: '))
d = float(input('거리(km) 입력: '))
t = getTime(s, d)
print(f'{s}(km/h)속도로 {d}(km) 이동한 시간: {t[0]}(h)시간 {t[1]}(m)분')
print('-' * 60)