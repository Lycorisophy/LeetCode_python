def maxScore(s: str) -> int:
    cnt0 = 0
    n = s.__len__()
    for i in s:
        if i == '0':
            cnt0 += 1
    cnt1 = n-cnt0

    dp = [0 for _ in range(n - 1)]
    dp[0] = cnt1 - 1 if s[0] == '1' else cnt1 + 1

    for i in range(1, n - 1):
        if s[i] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1] - 1

    return max(dp)


if __name__ == '__main__':
    print(maxScore("011101"))
    print(maxScore("00111"))
    print(maxScore("1111"))
