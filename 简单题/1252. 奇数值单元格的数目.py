def oddCells(m: int, n: int, indices: [[int]]) -> int:
    rows, cols = [False] * m, [False] * n
    for r, c in indices:
        rows[r] ^= True
        cols[c] ^= True
    res = 0
    for r in range(m):
        for c in range(n):
            if rows[r] ^ cols[c]:
                res += 1
    return res


if __name__ == '__main__':
    print(oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
    print(oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))

