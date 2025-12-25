class Solution(object):
    def differenceOfSums(self, n, m):
        a = []
        b = []
        for i in range(n+1):
            if i % m == 0:
                a.append(i)
            else:
                b.append(i)
        return sum(b)-sum(a)            