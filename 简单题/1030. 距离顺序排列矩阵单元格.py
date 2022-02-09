def allCellsDistOrder(R: int, C: int, r0: int, c0: int) -> [[int]]:
    res = []
    for r in range(R):
        for c in range(C):
            res.append([r, c])
    res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return res


if __name__ == '__main__':
    print(allCellsDistOrder(R=1, C=2, r0=0, c0=0))
    print(allCellsDistOrder(R=2, C=2, r0=0, c0=1))
    print(allCellsDistOrder(R=2, C=3, r0=1, c0=2))
