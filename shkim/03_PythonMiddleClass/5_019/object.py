# class PersonalComputer:
#     def __init__(self, name, cpu, memory, ssd):
#         self.name = name
#         self.cpu = cpu
#         self.memory = memory
#         self.ssd = ssd
#
#     def printPCInfo(self):
#         print(f'self.name: {self.name}')
#         print(f'self.cpu: {self.cpu}')
#         print(f'self.memory: {self.memory}')
#         print(f'self.ssd: {self.ssd}')
#
# myPC = PersonalComputer('myPC', 'i5', '16GB', '256GB')
# myPC.printPCInfo()
#
# myPC.memory = '32GB'
# myPC.printPCInfo()

class Calculator:

    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def add(self):
        self.result = self.number1 + self.number2
        return self.result

    def sub(self):
        self.result = self.number1 - self.number2
        return self.result

    def mul(self):
        self.result = self.number1 * self.number2
        return self.result

    def div(self):
        self.result = self.number1 / self.number2
        return self.result

myCal = Calculator()
myCal.number1 = 10
myCal.number2 = 20
print(f'calculator.add(): {myCal.add()}')
print(f'calculator.sub(): {myCal.sub()}')
print(f'calculator.mul(): {myCal.mul()}')
print(f'calculator.div(): {myCal.div()}')
