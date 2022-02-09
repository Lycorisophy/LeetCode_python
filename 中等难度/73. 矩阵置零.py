def setZeroes(matrix: [[int]]) -> None:
    n, m = matrix.__len__(), matrix[0].__len__()
    rows, cols = False, False
    for i in range(n):
        if matrix[i][0] == 0:
            rows = True
    for j in range(m):
        if matrix[0][j] == 0:
            cols = True
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(1, m):
                matrix[i][j] = 0
    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(1, n):
                matrix[i][j] = 0
    if rows:
        for i in range(n):
            matrix[i][0] = 0
    if cols:
        for j in range(m):
            matrix[0][j] = 0
    return matrix


if __name__ == '__main__':
    print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
