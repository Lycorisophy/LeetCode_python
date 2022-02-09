def mincostTickets(days: [int], costs: [int]) -> int:
    a, b, c = costs
    d = days[0]
    dp = [0 for _ in range(days[-1]-d+2)]
    n = len(dp)
    j = 0
    for i in range(1, n):
        if i == days[j]-d+1:
            dp[i] = min(dp[max(0, i - 1)] + a,
                        dp[max(0, i - 7)] + b,
                        dp[max(0, i - 30)] + c)
            j += 1
        else:
            dp[i] = dp[i - 1]
    return dp[-1]


if __name__ == '__main__':
    print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
