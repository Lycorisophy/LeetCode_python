def maxProfit(prices: [int]) -> int:
    n = prices.__len__()
    if n == 0:
        return 0
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0][0] = -prices[0]
    # f[i][0]: 手上持有股票的最大收益
    # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
    # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
        dp[i][1] = dp[i - 1][0] + prices[i]
        dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
    return max(dp[n - 1][1], dp[n - 1][2])


if __name__ == '__main__':
    print(maxProfit([1, 2, 3, 0, 2]))
