languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

uri = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_038/'
# for item in languages:
#     with open(uri + 'languages.txt', 'a') as f:
#         f.write(item + '\n')

# with open(uri + 'languages.txt', 'a') as f:
#     f.writelines(item + '\n' for item in languages)

scoreDic = {'kor': 85, 'eng': 85, 'mat': 85, 'sci': 85, 'his': 85}

for key in scoreDic.keys():
    with open(uri + 'scoreDic.txt', 'a') as f:
        f.write(key + ':\t' + str(scoreDic[key]) + '\n')

