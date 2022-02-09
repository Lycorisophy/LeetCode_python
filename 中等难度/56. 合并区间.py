def merge(intervals: [[int]]) -> [[int]]:
    n = intervals.__len__()
    if n == 1:
        return intervals
    intervals.sort(key=lambda x: [x[0], x[1]])
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            a, b = intervals[i], intervals[j]
            a1, a2 = a
            b1, b2 = b
            if a1 <= b1 <= a2:
                intervals[i] = [a1, max(a2, b2)]
                intervals.pop(j)
                n -= 1
            else:
                j += 1
        i += 1
    return intervals


if __name__ == '__main__':
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1, 4], [4, 5]]))
