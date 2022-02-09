def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    n = intervals.__len__()
    if n == 0:
        return [newInterval]
    s, e = newInterval
    i = 0
    do_insert = True
    while i < n:
        a = intervals[i]
        a1, a2 = a
        if s < a1:
            do_insert = False
            intervals.insert(i, newInterval)
            break
        else:
            i += 1
    if do_insert:
        intervals.append(newInterval)
    n += 1
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
    print(insert([[1,3],[6,9]],[2,5]))
    print(insert(intervals = [], newInterval = [5,7]))
    print(insert(intervals = [[1,5]], newInterval = [2,3]))
    print(insert(intervals = [[1,5]], newInterval = [2,7]))
