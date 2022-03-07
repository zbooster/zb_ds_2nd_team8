num1 = 10; num2 = 5

result = num1 > num2
print('num1 > num2 : {}'.format(result))

result = num1 >= num2
print('num1 >= num2 : {}'.format(result))

result = num1 < num2
print('num1 < num2 : {}'.format(result))

result = num1 <= num2
print('num1 <= num2 : {}'.format(result))

result = num1 == num2
print('num1 == num2 : {}'.format(result))

result = num1 != num2
print('num1 != num2 : {}'.format(result))

# userInput1 = int(input('첫 번째 숫자 입력: '))
# userInput2 = int(input('첫 번째 숫자 입력: '))
#
# print('{} > {} : {}'.format(userInput1, userInput2, (userInput1 > userInput2)))
# print('{} >= {} : {}'.format(userInput1, userInput2, (userInput1 >= userInput2)))
# print('{} < {} : {}'.format(userInput1, userInput2, (userInput1 < userInput2)))
# print('{} <= {} : {}'.format(userInput1, userInput2, (userInput1 <= userInput2)))
# print('{} == {} : {}'.format(userInput1, userInput2, (userInput1 == userInput2)))
# print('{} != {} : {}'.format(userInput1, userInput2, (userInput1 != userInput2)))

myCarLength = int(input('전장 길이 입력 : '))
myCarWidth = int(input('전폭 길이 입력 : '))

print('전장 가능 여부 : {}'.format((myCarLength<=5200)))
print('전폭 가능 여부 : {}'.format((myCarWidth<=1985)))
