# try:
#     inputData = input('input number:' )
#     numInt = int(inputData)
# except:
#     print('exception raise!!')
#     print('not number!!')
# else:
#     if numInt % 2 == 0:
#         print('even number!!')
#     else:
#         print('odd number!!')
#
# finally:
#     print(f'inputData: {inputData}')
#
#

dataList = []
floatList = []
evenList = []
oddList = []
n = 0

while n < 5:
    inputNum = input('input number: ')
    try:
        inputNum = float(inputNum)

    except:
        print('exception raise!!\ninput number again')

    else:
        if inputNum % 1 > 0:
            print('float number!')
            floatList.append(inputNum)

        elif inputNum % 2 == 0:
            print('even number!')
            evenList.append(int(inputNum))
        else:
            print('odd number!')
            oddList.append(int(inputNum))
        n += 1

    finally:
        dataList.append(inputNum)

print(f'evenList: {evenList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
print(f'dataList: {dataList}')