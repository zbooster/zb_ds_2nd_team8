defultPath = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_037/'

# file = open(defultPath + '5_037', 'a')
# file.write('python study')
# file.close()

# file = open(defultPath + '5_037', 'r')
# print(file.read())
# file.close()

# with open(defultPath + '5_037', 'a') as f:
#     f.write('python study')
#
# with open(defultPath + '5_037', 'r') as f:
#     print(f.read())

import random

def writeNumber(nums):
    for idx, num in enumerate(nums):
        with open(defultPath + 'lotto.txt', 'a') as f:
            if idx == len(nums) - 1:
                f.write('bonusstr(num))
            elif idx == len(nums) - 2:
                f.write(str(num) + ',')
            e