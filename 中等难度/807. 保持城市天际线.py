def maxIncreaseKeepingSkyline(grid: [[int]]) -> int:
    n = grid.__len__()
    m = grid[0].__len__()
    horizon = [0] * n
    vertical = [0] * m
    for i, row in enumerate(grid):
        horizon[i] = max(row)
    for j, col in enumerate(zip(*grid)):
        vertical[j] = max(col)
    res = 0
    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            res += min(horizon[i], vertical[j]) - h
    return res


if __name__ == '__main__':
    print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
    print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 0, 3], [0, 3, 1, 0]]))
    print(maxIncreaseKeepingSkyline([[3, 9, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 11]]))
