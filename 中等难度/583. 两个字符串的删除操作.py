def minDistance(word1: str, word2: str) -> int:
    M, N = len(word1), len(word2)
    dp = [0] * (N + 1)
    for i in range(1, M + 1):
        temp1 = dp[0]
        for j in range(1, N + 1):
            temp2 = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = temp1 + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            temp1 = temp2
    return M + N - 2 * dp[-1]



if __name__ == '__main__':
    print(minDistance("a", "b"))
    print(minDistance("seas", "seat"))
    print(minDistance("seat", "eastap"))
