def numSquares(n: int) -> int:
    dp = [0] * (n + 1)
    i = 1
    k = i * i
    while k <= n:
        dp[k] = 1
        i += 1
        k = i * i
    for i in range(2, n+1):
        if dp[i] == 0:
            mins = i
            m = i // 2 + 1
            for j in range(1, m):
                k = i - j
                mins = min(mins, dp[j] + dp[k])
            dp[i] = mins
    return dp[n]


if __name__ == '__main__':
    print(numSquares(10000))
