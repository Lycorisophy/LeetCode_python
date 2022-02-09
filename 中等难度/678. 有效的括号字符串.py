def checkValidString(s: str) -> bool:
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if s[i] == '*':
            dp[i][i] = True
    for i in range(n - 1):
        if s[i:i + 2] in ('()', '(*', '*)', '**'):
            dp[i][i + 1] = True
    for i in range(n-3, -1, -1):
        c1 = s[i]
        for j in range(i+2, n):
            c2 = s[j]
            if (c1 == '(' or c1 == '*') and (c2 == ')' or c2 == '*'):
                dp[i][j] = dp[i + 1][j - 1]
            for k in range(i, j):
                if not dp[i][j]:
                    dp[i][j] = dp[i][k] and dp[k + 1][j]
                else:
                    break
    return dp[0][n-1]


if __name__ == '__main__':
    print(checkValidString('(*))'))
    print(checkValidString('((*))'))
    print(checkValidString('(*(*))'))
