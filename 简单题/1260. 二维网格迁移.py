def shiftGrid(grid: [[int]], k: int) -> [[int]]:
    c = grid[0].__len__()
    grid = list(zip(*grid))
    for _ in range(k):
        tmp = grid[-1]
        for i in range(c-1, 0, -1):
            grid[i] = grid[i-1]
        grid[0] = tmp[-1:]+tmp[:-1]
    res = []
    for T in list(zip(*grid)):
        res.append([t for t in T])
    return res


if __name__ == '__main__':
    print(shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
    print(shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
    print(shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))
