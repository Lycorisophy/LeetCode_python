def numIslands(grid: [[str]]) -> int:
    if not grid:
        return 0
    n, m = grid.__len__(), grid[0].__len__()
    grid_sets = set()
    res = 0

    def dfs(x: int, y: int, sets: set()) -> set():
        if not 0 <= x < n or not 0 <= y < m or grid[x][y] != '1':
            return sets

        if (x, y) in sets:
            return sets
        sets.add((x, y))
        sets = dfs(x + 1, y, sets)
        sets = dfs(x - 1, y, sets)
        sets = dfs(x, y + 1, sets)
        sets = dfs(x, y - 1, sets)
        return sets

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                if (i, j) not in grid_sets:
                    grid_sets = dfs(i, j, grid_sets)
                    res += 1
    return res


if __name__ == '__main__':
    print(numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    ))
    print(numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ))
    print(numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "1", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ))
