# class Car01:
#
#     def drive(self):
#         print('drive() method called!!')
#
#
# class Car02:
#
#     def turbo(self):
#         print('turbo() method called!!')
#
#
# class Car03:
#
#     def fly(self):
#         print('fly() method called!!')
#
#
# class Car(Car01, Car02, Car03):
#
#     def __init__(self):
#         pass
#
# myCar = Car()
#
# myCar.drive()
# myCar.turbo()
# myCar.fly()

class BasicCalculator:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


class DeveloperCalculator:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2


class Calculator(BasicCalculator, DeveloperCalculator):

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


myCal = Calculator(10, 20)
print(myCal.add(10, 20))