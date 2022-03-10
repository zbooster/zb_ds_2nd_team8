# class Calculator:
#
#     def __init__(self, n1, n2):
#         print('[Calculator] __init__() colled!!')
#         self.num1 = n1
#         self.num2 = n2
#
#
# cal = Calculator(10, 20)
# print(f'cal.num1: {cal.num1}')
# print(f'cal.num2: {cal.num2}')
#
#

class P_Class:

    def __init__(self, pNum1, pNum2):
        print('[P_Class] __init__() called!!')
        self.pNum1 = pNum1
        self.pNum2 = pNum2


class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[C_Class] __init__() called!!')
        # P_Class.__init__(self, cNum1, cNum2)
        super().__init__(cNum1, cNum2)

        self.cNum1 = cNum1
        self.cNum2 = cNum2

cls = C_Class(10, 20)
