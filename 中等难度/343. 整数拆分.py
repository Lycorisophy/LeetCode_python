def integerBreak(n: int) -> int:
    dp = [1] * (n + 1)
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]


if __name__ == '__main__':
    print(integerBreak(10))

