def imageSmoother(M: [[int]]) -> [[int]]:
    r, c = len(M), len(M[0])
    res = [[0] * c for _ in range(r)]
    if r == 1:
        if c == 1:
            return M
        res[0][0] = int((M[0][0] + M[0][1]) / 2)
        res[0][-1] = int((M[0][-1] + M[0][-2]) / 2)
        for i in range(1, c - 1):
            res[0][i] = int((M[0][i - 1] + M[0][i] + M[0][i + 1]) / 3)
        return res
    elif c == 1:
        res[0][0] = int((M[0][0] + M[1][0]) / 2)
        res[-1][0] = int((M[-1][0] + M[-2][0]) / 2)
        for i in range(1, r - 1):
            res[i][0] = int((M[i - 1][0] + M[i][0] + M[i + 1][0]) / 3)
        return res
    res[0][0] = int((M[0][0] + M[0][1] + M[1][0] + M[1][1]) / 4)
    res[0][-1] = int((M[0][-1] + M[0][-2] + M[1][-1] + M[1][-2]) / 4)
    res[-1][0] = int((M[-1][0] + M[-1][1] + M[-2][0] + M[-2][1]) / 4)
    res[-1][-1] = int((M[-1][-1] + M[-1][-2] + M[-2][-1] + M[-2][-2]) / 4)
    for i in range(1, c - 1):
        res[0][i] = int((M[0][i-1] + M[0][i] + M[0][i+1] + M[1][i-1] + M[1][i] + M[1][i+1]) / 6)
    for i in range(1, c - 1):
        res[-1][i] = int((M[-1][i - 1] + M[-1][i] + M[-1][i + 1] + M[-2][i - 1] + M[-2][i] + M[-2][i + 1]) / 6)
    for i in range(1, r - 1):
        res[i][0] = int((M[i - 1][0] + M[i][0] + M[i + 1][0] + M[i - 1][1] + M[i][1] + M[i + 1][1]) / 6)
    for i in range(1, r - 1):
        res[i][-1] = int((M[i - 1][-1] + M[i][-1] + M[i + 1][-1] + M[i - 1][-2] + M[i][-2] + M[i + 1][-2]) / 6)
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            res[i][j] = int((M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1]
                             + M[i][j - 1] + M[i][j] + M[i][j + 1]
                             + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) / 9)
    return res


if __name__ == '__main__':
    print(imageSmoother([[7],[9],[6]]))

