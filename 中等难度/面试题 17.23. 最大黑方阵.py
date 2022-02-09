def findSquare(matrix: [[int]]) -> [int]:
    def isSquare(r, c, n):
        for j in range(r, r + n):
            if matrix[j][c] == 1 or matrix[j][c+n-1] == 1:
                return False
        for k in range(c+1, c + n-1):
            if matrix[r][k] == 1 or matrix[r+n-1][k] == 1:
                return False
        return True

    N = len(matrix)
    i = 1
    while i <= N:
        n = N - i + 1
        for r in range(i):
            for c in range(i):
                if isSquare(r, c, n):
                    return [r, c, n]
        i += 1
    return []


if __name__ == '__main__':
    print(findSquare([
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]))
    print(findSquare([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]))
    print(findSquare([
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]))
