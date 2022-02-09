def minCost(costs: [[int]]) -> int:
    n = len(costs)
    dp = [[2000 for _ in range(3)] for _ in range(n)]
    dp[0] = [cost for cost in costs[0]]
    for i in range(1, n):
        for j in range(3):
            cost = costs[i][j]
            for k in range(3):
                if k != j:
                    dp[i][j] = min(dp[i-1][k]+cost, dp[i][j])
    return min(dp[-1])


if __name__ == '__main__':
    print(minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
    print(minCost(costs=[[7, 6, 2]]))
