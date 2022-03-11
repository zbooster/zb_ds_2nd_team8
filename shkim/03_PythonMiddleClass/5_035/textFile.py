defultPath = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_035/'

# file = open(defultPath + 'text.txt', 'r')
#
# str = file.read()
# print(f'str: {str}')
#
# file.close()

file = open(defultPath + 'test.txt', 'r', encoding='UTF-8')

str = file.read()
print(f'str: {str}')

file.close()

str = str.replace('Python', '파이썬', 2)
print(f'str: {str}')

file = open(defultPath + 'test.txt', 'w', encoding='UTF-8')
file.write(str)

file.close()