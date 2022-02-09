def transpose(matrix: [[int]]) -> [[int]]:
    m, n = len(matrix), len(matrix[0])
    res = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][i] = matrix[i][j]
    return res


if __name__ == '__main__':
    print(transpose([[1,2,3],[4,5,6],[7,8,9],[0,0,0]]))
