import random


class Car:

    def __init__(self, n='fire car', c='red', s='200'):
        self.name = n
        self.color = c
        self.speed = s
        self.distance = 0

    def printCarInfo(self):
        print(f'name: {self.name}: color: {self.color}, speed: {self.speed}')

    def controlSpeed(self):
        return random.randint(0, self.speed)

    def getDistanceForHour(self):
        return self.controlSpeed() * 1


class CarRacing:

    def __init__(self):
        self.cars = []
        self.rankings = []

    def startRacing(self):
        for i in range(10):
            print(f'Racing: {i+1}바퀴')
            for car in self.cars:
                car.distance += car.getDistanceForHour()

    def printCurrentCarDistance(self):
        for car in self.cars:
            print(f'{car.name}: {car.distance}', end='\t')
        print()

    def addCar(self, c):
        self.cars.append(c)