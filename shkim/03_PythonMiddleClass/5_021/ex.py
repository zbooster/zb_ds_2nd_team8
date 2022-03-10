plaOriSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOriSco.copy()

maxVal = max(plaOriSco)
minVal = min(plaOriSco)

plaCopSco.remove(maxVal)
plaCopSco.remove(minVal)

plaOriSco.sort()
plaCopSco.sort()

print(f'plaOriSco: {plaOriSco}')
print(f'plaOriSco: {plaCopSco}')
print(f'Original Total: {sum(plaOriSco)}')
print(f'Original Average: {sum(plaOriSco)/len(plaOriSco)}')
print(f'Copy Total: {sum(plaCopSco)}')
print(f'Copy Average: {sum(plaCopSco)/len(plaCopSco)}')
print(f'oriAvg - copAvg: {sum(plaOriSco)/len(plaOriSco) - sum(plaCopSco)/len(plaCopSco)}')