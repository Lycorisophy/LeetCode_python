def stoneGame(piles: [int]) -> bool:
    n = len(piles)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    for i in range(1, n):
        for j in range(n-i):
            dp[j][j+i] = max(piles[j]-dp[j+1][j+i], piles[j+i]-dp[j][j+i-1])
    return dp[0][n-1] > 0


if __name__ == '__main__':
    print(stoneGame([5, 3, 4, 5]))
    print(stoneGame([5, 3, 11, 13, 4, 5]))
    print(stoneGame([13, 5, 3, 11, 13, 4, 5, 11]))
