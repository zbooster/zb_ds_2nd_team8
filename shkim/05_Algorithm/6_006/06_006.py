# import random
#
# midStuScos = random.sample(range(50, 101), 20)
# midRanks = [0 for i in range(len(midStuScos))]
# endStuScos = random.sample(range(50, 101), 20)
# endRanks = [0 for i in range(len(endStuScos))]
#
# print(f'midStuScos: {midStuScos}')
# print(f'midRanks: {midRanks}')
# print(f'endStuScos: {endStuScos}')
# print(f'endRanks: {endRanks}')
#
# for idx, num1 in enumerate(midStuScos):
#     for num2 in midStuScos:
#         if num1 < num2:
#             midRanks[idx] += 1
#
# for idx, num1 in enumerate(endStuScos):
#     for num2 in endStuScos:
#         if num1 < num2:
#             endRanks[idx] += 1
#
# for i in range(20):
#     deviation = endRanks[i] - midRanks[i]
#     if deviation > 0:
#         deviation = '↑' + str(deviation)
#     elif deviation < 0:
#         deviation = '↓' + str(abs(deviation))
#     elif deviation == 0:
#         deviation = '=' + str(deviation)
#     print(f'midRanks: {midRanks[i]} \t endRanks: {endRanks[i]}\t Deviation:{deviation}')
