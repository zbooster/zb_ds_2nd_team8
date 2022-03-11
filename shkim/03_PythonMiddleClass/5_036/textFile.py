defultPath = 'C:/pythonEx/zb_ds_2nd_team8/shkim/03_PythonMiddleClass/5_036/'

# 'w' 파일 모드
# file = open(defultPath + 'hello.txt', 'w')
# file.write('Hello python!!')
# file.close()

# 'a' 파일 모드
# file = open(defultPath + 'hello.txt', 'a')
# file.write('\nNice to meet you')
# file.close()

# 'x' 파일 모드
# file = open(defultPath + 'hello_01.txt', 'x')
# file.write('Nice to meet you')
# file.close()

# 'r' 파일 모드
# file = open(defultPath + 'hello_01.txt', 'r')
# str = file.read()
# print(str)
# file.close()

def writePrimeNumber(n):
    file = open(defultPath + 'prime_number.txt', 'a')
    file.write(str(n))
    file.write('\n')

    file.close()

inputNum = int(input('0보다 큰 정수 입력: '))
for number in range(2, (inputNum + 1)):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break

    if flag:
        writePrimeNumber(number)

