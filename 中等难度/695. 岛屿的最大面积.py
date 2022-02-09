def maxAreaOfIsland(grid: [[int]]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0
    visited = set()

    def dfs(x: int, y: int, cnt: int) -> int:
        if not 0 <= x < n or not 0 <= y < m or grid[x][y] != 1 or (x, y) in visited:
            return cnt
        visited.add((x, y))
        cnt += 1
        cnt = dfs(x + 1, y, cnt)
        cnt = dfs(x - 1, y, cnt)
        cnt = dfs(x, y + 1, cnt)
        cnt = dfs(x, y - 1, cnt)
        return cnt

    for i, row in enumerate(grid):
        for j, d in enumerate(row):
            if d == 1 and (i, j) not in visited:
                c = dfs(i, j, 0)
                res = max(res, c)
    return res


if __name__ == '__main__':
    print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
                          ))
    print(maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
