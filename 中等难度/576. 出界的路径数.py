def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    if maxMove == 0:
        return 0
    dp = [[[0] * (n+2) for _ in range(m+2)] for _ in range(maxMove+1)]
    dp[0][startRow+1][startColumn+1] = 1
    res = 0
    for i in range(1, maxMove+1):
        for j in range(m+2):
            for k in range(n+2):
                j1, j2 = j + 1, j - 1
                k1, k2 = k + 1, k - 1
                if 1 <= j1 <= m and 1 <= k <= n:
                    dp[i][j][k] += dp[i-1][j1][k]
                if 1 <= j2 <= m and 1 <= k <= n:
                    dp[i][j][k] += dp[i-1][j2][k]
                if 1 <= k1 <= n and 1 <= j <= m:
                    dp[i][j][k] += dp[i-1][j][k1]
                if 1 <= k2 <= n and 1 <= j <= m:
                    dp[i][j][k] += dp[i-1][j][k2]
                if j == 0 or j == m+1 or k == 0 or k == n+1:
                    res += dp[i][j][k]
    return res % (10**9+7)


if __name__ == '__main__':
    print(findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
    print(findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
