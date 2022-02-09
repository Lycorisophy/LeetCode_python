def orderOfLargestPlusSign(n: int, mines: [[int]]) -> int:
    l = [[1 for _ in range(n)] for _ in range(n)]
    for i in mines:
        l[i[0]][i[1]] = 0
    dp = [[[0, 0, 0, 0] for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):  # 先正向遍历
        for j in range(n):
            if l[i][j] == 0:
                continue
            else:
                dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
                dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):  # 逆向遍历
            if l[i][j] == 0:
                continue
            else:
                dp[i + 1][j + 1][2] = dp[i + 2][j + 1][2] + 1
                dp[i + 1][j + 1][3] = dp[i + 1][j + 2][3] + 1
    m = max([max([min(i) for i in j]) for j in dp])
    return m


if __name__ == '__main__':
    print(orderOfLargestPlusSign(5, mines=[[3, 0], [3, 3]]))
    print(orderOfLargestPlusSign(2, mines=[]))
    print(orderOfLargestPlusSign(1, mines=[[0, 0]]))
