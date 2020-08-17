def getpartialmatch(N):
    m = len(N)
    pi = [0] * m
    begin = 1
    matched = 0
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


class KMP:
    def __init__(self, incruit, thinkgood):
        self.incruit = incruit
        self.thinkgood = thinkgood
        self.contests = thinkgood
        self.ret = list()

    def check(self):
        for elem1 in list(self.thinkgood.keys()):
            for elem2 in self.incruit.keys():
                self.kmp(elem1, elem2) if len(elem1) > len(elem2) else self.kmp(elem2, elem1)
                if not self.ret:
                    self.contests[elem2] = self.incruit[elem2]
                    break
                else:
                    del self.ret[:]

    def kmp(self, H, N):
        n = len(H)
        m = len(N)
        pi = getpartialmatch(N)
        begin = 0
        matched = 0
        while begin <= n - m:
            if matched < m and H[begin + matched] == N[matched]:
                matched += 1
                if matched == m:
                    self.ret.append(begin)
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - pi[matched - 1]
                    matched = pi[matched - 1]
                    