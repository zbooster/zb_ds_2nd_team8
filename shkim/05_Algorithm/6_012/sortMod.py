class sortNumber:

    def __init__(self, ns, asc=True):
        self.nums = ns
        self.isAsc = asc

    def isAscending(self, flag=True):
        self.isAsc = flag

    def setSort(self):
        for i in range(len(self.nums)):
            minIdx = i
            for j in range(i+1, len(self.nums)):
                if self.isAsc:
                    if self.nums[minIdx] > self.nums[j]:
                        minIdx = j
                else:
                    if self.nums[minIdx] < self.nums[j]:
                        minIdx = j

            self.nums[i], self.nums[minIdx] = self.nums[minIdx], self.nums[i]

    def getSortedNum(self):
        return self.nums


