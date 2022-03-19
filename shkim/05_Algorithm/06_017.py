class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum
    def getMaxNum(self):
        self.maxNum = self.nums[0]

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n

        return self.maxNum

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

