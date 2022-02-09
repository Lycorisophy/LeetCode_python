def minPathSum(grid: [[int]]) -> int:
    n = grid.__len__()
    m = grid[0].__len__()
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[n - 1][m - 1]


if __name__ == '__main__':
    print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(minPathSum([[1, 2, 3], [4, 5, 6]]))
    print(minPathSum([[1, 5, 5], [5, 5, 1], [4, 2, 1]]))
