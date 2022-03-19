class sortNumbers:

    def __init__(self, ns, asc=True):
        self.nums = ns
        self.isAsc = asc

    def isAscending(self, flag):
        self.isAsc = flag

    def setSort(self):

        for i1 in range(1, len(self.nums)):
            i2 = i1 - 1
            cNum = self.nums[i1]

            if self.isAsc:
                while self.nums[i2] > cNum and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1
            else:
                while self.nums[i2] < cNum and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1

            self.nums[i2 + 1] = cNum

    def getSortedNumbers(self):
        return self.nums

    def getMinNumber(self):
        if self.isAsc:
            return self.nums[0]
        else:
            return self.nums[len(self.nums) - 1]

    def getMaxNumber(self):
        if self.isAsc:
            return self.nums[len(self.nums) - 1]
        else:
            return self.nums[0]


# import copy
#
#
# def bubbleSort(ns, deepCopy=True):
#
#     if deepCopy:
#         cns = copy.copy(ns)
#     else:
#         cns = ns
#
#     length = len(cns) - 1
#     for i in range(length):
#         for j in range(length - i):
#             if cns[j] > cns[j + 1]:
#                 cns[j], cns[j + 1] = cns[j + 1], cns[j]
#
#     return cns