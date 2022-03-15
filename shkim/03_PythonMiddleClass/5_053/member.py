class Member:
    def __init__(self, i, p):
        self.id = i
        self.pw = p


class MemberRepository:
    def __init__(self):
        self.members = {}

    def addMember(self, m):
        self.members[m.id] = m.pw

    def loginMember(self, i, p):
        isMember = i in self.members
        if isMember and self.members[i] == p:
            print('Log-in success!!')
        else:
            print('Log-in fail!!')

    def removeMember(self, i, p):
        del self.members[i]

    def printMembers(self):
        for mk in self.members.keys():
            print('ID: {}'.format(mk))
            print('PW: {}'.format(self.members[mk]))


if __name__ == '__main__':
    mems = MemberRepository()
    mem = Member('abc@gmail.com', '1234')
    mems.addMember(mem)