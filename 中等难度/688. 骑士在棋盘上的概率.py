def knightProbability(n: int, k: int, row: int, column: int) -> float:
    if k == 0:
        return 1
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k)]
    for i in range(n):
        for j in range(n):
            dp[0][i][j] = 1
    for x in range(1, k):
        for y in range(n):
            for z in range(n):
                for Y, Z in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                             (1, 2), (1, -2), (-1, 2), (-1, -2)):
                    if 0 <= y + Y < n and 0 <= z + Z < n:
                        dp[x][y][z] += dp[x - 1][y + Y][z + Z] / 8
    res = 0
    for Y, Z in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)):
        if 0 <= row + Y < n and 0 <= column + Z < n:
            res += dp[k - 1][row + Y][column + Z] / 8
    return res


if __name__ == '__main__':
    print(knightProbability(n=3, k=2, row=0, column=0))
    print(knightProbability(n=1, k=0, row=0, column=0))
