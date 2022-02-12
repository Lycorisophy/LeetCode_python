def numEnclaves(grid: [[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m < 3 or n < 3:
        return 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:
            return
        vis[r][c] = True
        for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            dfs(x, y)

    vis = [[False] * n for _ in range(m)]
    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)
    for j in range(1, n - 1):
        dfs(0, j)
        dfs(m - 1, j)
    return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))


if __name__ == '__main__':
    print(numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    print(numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
