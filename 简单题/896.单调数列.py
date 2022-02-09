def isMonotonic(A: [int]) -> bool:
    n = A.__len__()
    if n < 3:
        return True
    pre = A[1]
    begin = A[0]
    if begin < pre:
        trend = 1
    elif begin == pre:
        trend = 0
    else:
        trend = -1
    for a in A[2:]:
        if pre < a:
            if trend == -1:
                return False
            if trend == 0:
                trend = 1
            pre = a
        elif pre > a:
            if trend == 1:
                return False
            if trend == 0:
                trend = -1
            pre = a
    return True


if __name__ == '__main__':
    print(isMonotonic([1, 2, 2, 3]))
    print(isMonotonic([6, 5, 4, 4]))
    print(isMonotonic([1, 3, 2]))
    print(isMonotonic([1, 2, 4, 5]))
    print(isMonotonic([1, 1, 1]))
