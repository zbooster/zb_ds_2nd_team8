# from abc import ABCMeta
# from abc import abstractmethod
#
# class AirPlane(metaclass=ABCMeta):
#
#     @abstractmethod
#     def flight(self):
#         pass
#
#     def forward(self):
#         print('전진!!')
#
#     def backward(self):
#         print('후진!!')
#
#
# class AirLiner(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 400km/h 비행!!')
#
#
# class FighterPlane(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 700km/h 비행!!')
#
#
# al = AirLiner('red')
# al.flight()
#
# af = FighterPlane('blue')
# af.flight()

from abc import ABCMeta
from abc import abstractmethod


class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass


class DeveloperCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def mod(self, n1, n2):
        print(n1 % n2)

    def flo(self, n1, n2):
        print(n1 // n2)


myCal = DeveloperCalculator()
myCal.add(1, 2)