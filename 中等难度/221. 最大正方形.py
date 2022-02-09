def maximalSquare(matrix: [[str]]) -> int:
    n, m = matrix.__len__(), matrix[0].__len__()
    res = 0
    length = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                length = 1
                all_one = True
                ei, ej = i + 1, j + 1
                while ei < n and ej < m:
                    for a in range(i, ei+1):
                        if matrix[a][ej] == '0':
                            all_one = False
                            break
                    if all_one:
                        for b in range(j, ej + 1):
                            if matrix[ei][b] == '0':
                                all_one = False
                                break
                    if all_one:
                        length += 1
                        ei += 1
                        ej += 1
                    else:
                        break
            res = max(length, res)
    return res * res


if __name__ == '__main__':
    print(maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(maximalSquare([["0", "1"], ["1", "0"]]))
    print(maximalSquare([["0"]]))
