def PredictTheWinner(nums: [int]) -> bool:
    n = nums.__len__()
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i, num in enumerate(nums):
        dp[i][i] = num
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
    return dp[0][n-1] >= 0


if __name__ == '__main__':
    print(PredictTheWinner([1, 5, 2]))
    print(PredictTheWinner([1, 5, 233, 7]))

