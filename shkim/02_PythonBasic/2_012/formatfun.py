userName = 'Hong gil dong'
userAge = 21

print(userName)
print(userAge)

print('User name : {}'.format(userName))
print('User age : {}'.format(userAge))

print('User name: {}, User age: {}'.format(userName, userAge))
print('User name: {1}, User age: {0}'.format(userName, userAge))

print('나의 이름은 {}이고, 나이는 {}살 입니다. {}이름은 아버님께서 지어 주셨습니다.'
      .format(userName, userAge, userName))

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어 주셨습니다.'
      .format(userName, userAge))

print('User name : %s' % userName)
print('User age : %d' % userAge)

print('User name : %s, User age : %d ' % (userName, userAge))

pi = 3.14

print('pi : %f' % pi)
print('pi : %.2f' % pi)

print('pi : %d' % pi)

radius = float(input('반지름 입력: '))
pi = float(input('원주율 입력: '))
circleArea = radius * radius * pi

print('radius %.2f' % radius)
print('pi %.2f' % pi)
print('circleArea : %.2f' % circleArea)