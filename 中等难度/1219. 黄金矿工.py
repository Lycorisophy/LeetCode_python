from functools import lru_cache


def getMaximumGold(grid: [[int]]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0

    def dfs(x: int, y: int) -> int:
        if x < 0 or y < 0 or x == n or y == m or not grid[x][y]:
            return 0
        record = grid[x][y]
        grid[x][y] = mx = 0
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            mx = max(mx, dfs(x + dx, y + dy))
        grid[x][y] = record
        return record + mx

    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i, j))
    return res


if __name__ == '__main__':
    print(getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
    print(getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
