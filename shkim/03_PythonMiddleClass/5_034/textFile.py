# import sys
# print(sys.path)

# file = open('C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_034/text.txt', 'w')
#
# strCnt = file.write('Hello Python!')
# print(f'strCnt: {strCnt}')
#
# file.close()

defultPath = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_034/'

import time

lt = time.localtime()
dateStr = '[' + str(lt.tm_year) + '년' + \
    str(lt.tm_mon) + '월' + \
    str(lt.tm_mday) + '일] '

dateStr = time.strftime('[%Y-%m-%d %H:%M:%S %p]')

todaySchedule = input('오늘 일정: ')

file = open(defultPath + 'test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()