num = int(input('반지름(cm) 입력: '))

circleArea = num * num * 3.14
circleLength = 2 * num * 3.14

print('원의 넓이\t: %dcm' % (circleArea))
print('원 둘레길이\t: %dcm' % (circleLength))
print('원의 넓이\t: %.1fcm' % (circleArea))
print('원 둘레길이\t: %.1fcm' % (circleLength))
print('원의 넓이\t: %.3fcm' % (circleArea))
print('원 둘레길이\t: %.3fcm' % (circleLength))
