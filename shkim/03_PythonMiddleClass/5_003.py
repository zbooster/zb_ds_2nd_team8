# def fun1():
#     print('fun1 호출!')
#     fun2()
#
# def fun2():
#     print('fun2 호출!')
#     fun3()
#
# def fun3():
#     print('fun3 호출!')
#
# fun1()

# def printTodayWeather():
#     pass
#
# printTodayWeather()

def gugudan(x):
    if x < 6:
        for i in range(1, 10):
            print('{} x {} = {}'.format(x, i, (x*i)))
        gugudan(x+1)

gugudan(2)

