def searchMatrix(matrix: [[int]], target: int) -> bool:
    n, m = matrix.__len__(), matrix[0].__len__()
    L, R = 0, n*m - 1
    while L <= R:
        M = L + (R - L) // 2
        r, c = divmod(M, m)
        num = matrix[r][c]
        if num > target:
            R = M - 1
        elif num < target:
            L = M + 1
        elif num == target:
            return True
    return False


if __name__ == '__main__':
    print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
