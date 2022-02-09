def searchMatrix(matrix: [[int]], target: int) -> bool:
    n, m = len(matrix), len(matrix[0])
    for nums in matrix:
        if nums[0] == target:
            return True
        if nums[0] < target:
            L, R = 0, m - 1
            while L <= R:
                M = L + (R - L) // 2
                if nums[M] > target:
                    R = M - 1
                elif nums[M] < target:
                    L = M + 1
                elif nums[M] == target:
                    return True
    return False


if __name__ == '__main__':
    print(searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
    print(searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
