def restoreArray(adjacentPairs: [[int]]) -> [int]:
    l = len(adjacentPairs)


    if adjacentPairs[0][0] in adjacentPairs[1]:
        adjacentPairs[0][0], adjacentPairs[0][1] = adjacentPairs[0][1], adjacentPairs[0][0]
    for i in range(len(adjacentPairs) - 1):
        if adjacentPairs[i][1] == adjacentPairs[i + 1][1]:
            adjacentPairs[i + 1][0], adjacentPairs[i + 1][1] = adjacentPairs[i + 1][1], adjacentPairs[i + 1][0]
    res = []
    for pair in adjacentPairs:
        res.append(pair[0])
    res.append(adjacentPairs[-1][1])
    return res


if __name__ == '__main__':
    print(restoreArray([[4,-2],[1,4],[-3,1]]))
