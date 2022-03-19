from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary(metaclass=ABCMeta):


    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registWord(self, w1, w2):
        pass

    @abstractmethod
    def removeWord(self, w1):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass

    @abstractmethod
    def searchWord(self, w1):
        pass


class KorToEng(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToEng] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1, w2):
        print(f'[KorToEng] removeWord() : {w1}')
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f'[KorToEng] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f'[KorToEng] searchWord() : {w1}')
        return self.wordDic[w1]


class KorToJan(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToJan] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1, w2):
        print(f'[KorToJan] removeWord() : {w1}')
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f'[KorToJan] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f'[KorToJan] searchWord() : {w1}')
        return self.wordDic[w1]



if __name__ == '__main__':
    korJanDic = KorToJan()
    korEngDic = KorToEng()

    korJanDic.registWord('하나', '一つ')
    korJanDic.registWord('둘', '二つ')
    print(korJanDic.searchWord('둘'))

    korEngDic.registWord('하나', 'one')
    korEngDic.registWord('둘', 'two')
    print(korEngDic.searchWord('둘'))


