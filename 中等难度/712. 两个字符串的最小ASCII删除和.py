def minimumDeleteSum(s1: str, s2: str) -> int:
    M, N = len(s1), len(s2)
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(M-1, -1, -1):
        dp[i][N] = dp[i+1][N] + ord(s1[i])
    for j in range(N-1, -1, -1):
        dp[M][j] = dp[M][j+1] + ord(s2[j])
    for i in range(M-1, -1, -1):
        for j in range(N-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j]+ord(s1[i]), dp[i][j+1]+ord(s2[j]))
    return dp[0][0]


if __name__ == '__main__':
    print(minimumDeleteSum(s1="sea", s2="eat"))
    print(minimumDeleteSum(s1="delete", s2="leet"))
