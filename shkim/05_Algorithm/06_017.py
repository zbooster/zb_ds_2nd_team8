class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum < n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum





nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

