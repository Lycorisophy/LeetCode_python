def isInterleave(s1: str, s2: str, s3: str) -> bool:
    s1, s2, s3 = list(s1), list(s2), list(s3)
    n1, n2, n3 = s1.__len__(), s2.__len__(), s3.__len__()
    if n1 + n2 != n3:
        return False
    dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
    dp[0][0] = True
    for i in range(0, n1+1):
        for j in range(0, n2+1):
            p = i + j - 1
            if i > 0:
                dp[i][j] = (dp[i-1][j] and (s1[i-1] == s3[p])) or dp[i][j]
            if j > 0:
                dp[i][j] = (dp[i][j-1] and (s2[j-1] == s3[p])) or dp[i][j]
    return dp[-1][-1]


if __name__ == '__main__':
    print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(isInterleave(s1="", s2="", s3=""))
