def maxProfit(prices: [int], fee: int) -> int:
    n = prices.__len__()
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    return dp[n - 1][0]


if __name__ == '__main__':
    print(maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
    print(maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
