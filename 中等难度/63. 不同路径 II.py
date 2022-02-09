def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
    n = obstacleGrid.__len__()
    m = obstacleGrid[0].__len__()
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i, char in enumerate(obstacleGrid[0]):
        if char != 1:
            dp[0][i] = 1
        else:
            break
    for i in range(0, n):
        if obstacleGrid[i][0] != 1:
            dp[i][0] = 1
        else:
            break
    for i in range(1, n):
        for j in range(1, m):
            char = obstacleGrid[i][j]
            if char == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]


if __name__ == '__main__':
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 0, 0]]))

