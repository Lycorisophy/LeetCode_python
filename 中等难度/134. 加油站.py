def canCompleteCircuit(gas: [int], cost: [int]) -> int:
    n = gas.__len__()
    i = 0
    while i < n:
        j = i
        res = gas[j] - cost[j]
        if res >= 0:
            if j != n - 1:
                j += 1
            else:
                j = 0
            while j != i:
                res = res + gas[j] - cost[j]
                if res >= 0:
                    if j != n - 1:
                        j += 1
                    else:
                        j = 0
                else:
                    i += 1
                    break
            if res >= 0:
                return i
        else:
            i += 1
    return -1


if __name__ == '__main__':
    print(canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
