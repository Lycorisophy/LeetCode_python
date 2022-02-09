def prefixesDivBy5(A: [int]) -> [bool]:
    s = 0
    res = []
    for a in A:
        s = ((s << 1) + a) % 5
        res.append(not s)
    return res


if __name__ == '__main__':
    print(prefixesDivBy5([0, 1, 1]))
    print(prefixesDivBy5([1, 1, 1]))
    print(prefixesDivBy5([0, 1, 1, 1, 1, 1]))
    print(prefixesDivBy5([1, 1, 1, 0, 1]))
