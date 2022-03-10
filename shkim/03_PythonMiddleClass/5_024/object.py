class MidExam:

    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_mat_score = s3


    def midTotal(self):
        return self.mid_kor_score + self.mid_eng_score + self.mid_mat_score

    def midAverage(self):
        return self.midTotal() / 3

    def printMidScore(self):
        print(f'MidExam Total: {total}')
        print(f'MidExam Average : {average}')



class EndExam(MidExam):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')
        super().__init__(s1, s2, s3)

        self.end_kor_score = s4
        self.end_eng_score = s5
        self.end_mat_score = s6

