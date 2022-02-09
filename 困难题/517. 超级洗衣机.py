def findMinMoves(machines: [int]) -> int:
    n = len(machines)
    total = sum(machines)
    if total % n != 0:
        return -1
    ave = total // n
    res, s = 0, 0
    for machine in machines:
        machine -= ave
        s += machine
        res = max(res, abs(s), machine)
    return res


if __name__ == '__main__':
    print(findMinMoves([1, 0, 5]))
    print(findMinMoves([0, 3, 0]))
    print(findMinMoves([0, 2, 0]))
    print(findMinMoves([0]*98+[99]))
