import math


def getMoneyAmount(n: int) -> int:
    if n == 1:
        return 0
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i+1] = i
    for L in range(n, -1, -1):
        for R in range(L + 1, n + 1):
            tmp = math.inf
            for mid in range(L, R):
                tmp = min(tmp, mid + max(dp[L][mid - 1], dp[mid + 1][R]))
            dp[L][R] = tmp

    return dp[1][n]


if __name__ == '__main__':
    print(getMoneyAmount(10))

