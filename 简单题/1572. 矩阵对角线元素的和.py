def diagonalSum(mat: [[int]]) -> int:
    n = mat.__len__()
    res = 0
    if n % 2 == 0:
        for i, m in enumerate(mat):
            res += m[i]
            res += m[-i-1]
    else:
        mid = n // 2
        for i, m in enumerate(mat):
            if i == mid:
                res += m[i]
            else:
                res += m[i]
                res += m[-i-1]
    return res


if __name__ == '__main__':
    print(diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]]))
    print(diagonalSum([[1,1,1,1],
          [1,1,1,1],
       [1,1,1,1],
        [1,1,1,1]]
))
    print(diagonalSum([[5]]))
