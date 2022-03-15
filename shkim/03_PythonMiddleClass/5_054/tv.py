class NormalTv:
    def __init__(self, i, c, r):
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTv = False
        self.aiTv = False

    def turnOn(self):
        print('TV가 켜졌습니다.')

    def turnOff(self):
        print('TV가 꺼졌습니다.')

    def printTvInfo(self):
        print('inch: {}'.format(self.inch))
        print('color: {}'.format(self.color))
        print('resolution: {}'.format(self.resolution))
        print('smartTv: {}'.format(self.smartTv))
        print('aiTv: {}'.format(self.aiTv))


class Tv4K(NormalTv):
    def __init__(self, i, c, r):
        super().inch = i
        super().color = c
        super().resolution = r

    def setSmartTv(self):
        super().smartTv = True


class Tv8K(NormalTv):
    def __init__(self, i, c, r):
        super().__init__(i, c, r)

    def setSmartTv(self):
        super().smartTv = True

    def setAiTv(self):
        super().aiTv = True
