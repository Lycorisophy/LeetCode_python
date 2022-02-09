class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.n = 0

    def addNum(self, val: int) -> None:
        L, R = 0, self.n - 1
        while L <= R:
            m = L + (R - L) // 2
            if self.intervals[m] > val:
                R = m - 1
            elif self.intervals[m] < val:
                L = m + 1
            elif self.intervals[m] == val:
                return
        self.intervals.insert(L, val)
        self.n += 1

    def getIntervals(self) -> [[int]]:
        out = []
        left = self.intervals[0]
        for i in range(1, len(self.intervals)):
            if self.intervals[i] == self.intervals[i - 1] + 1:
                continue
            else:
                out.append([left, self.intervals[i - 1]])
                left = self.intervals[i]
        out.append([left, self.intervals[-1]])
        return out


if __name__ == '__main__':
    summaryRanges = SummaryRanges()
    print(summaryRanges.addNum(1))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(3))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(7))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(2))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(6))
    print(summaryRanges.getIntervals())

