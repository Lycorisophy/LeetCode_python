def partition(s: str) -> [[str]]:
    n = s.__len__()
    dp = [[True for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

    res = []
    ans = []

    def backtrack(i: int):
        if i == n:
            res.append(ans[:])
        for j in range(i, n):
            if dp[i][j]:
                ans.append(s[i:j+1])
                backtrack(j+1)
                ans.pop()

    backtrack(0)
    return res


if __name__ == '__main__':
    print(partition('aabaabcc'))
    print(partition("aab"))
    print(partition("a"))
