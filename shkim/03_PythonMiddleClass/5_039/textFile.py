uri = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_039/'

# with open(uri + 'lans.txt', 'r') as f:
#     lanList = f.readlines()
#
# print(f'lanList : {lanList}')
# print(f'lanList type : {type(lanList)}')
#
# with open(uri + 'lans.txt', 'r') as f:
#     line = f.readline()
#
#     while line != '':
#         print(f'line: {line}', end='')
#         line = f.readline()

scoreDic = {}

with open(uri + 'scores.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':')
        scoreDic[tempList[0]] = int(tempList[1].strip('\n'))
        line = f.readline()

print(f'scoreDic: {scoreDic}')