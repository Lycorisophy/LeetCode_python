def surfaceArea(grid: [[int]]) -> int:
    n = len(grid)
    s1, s2, s3 = 0, 0, 0
    grid2 = [[0 for _ in range(n)] for _ in range(n)]

    def para_surface(span: [int], n: int) -> int:
        res = 0
        base = span[0]
        pre = base
        res += base
        if n == 1:
            return res
        is_increase = 1
        for i in range(1, n):
            tmp = span[i]
            if tmp < pre and is_increase == 0:
                pre = tmp
            elif tmp < pre and is_increase == 1:
                is_increase = 0
                res += pre - base
                pre = tmp
            elif tmp >= pre and is_increase == 0:
                base = pre
                is_increase = 1
                pre = tmp
            elif tmp >= pre and is_increase == 1:
                pre = tmp
        return res if is_increase == 0 else res + pre - base

    for i, span in enumerate(grid):
        s2 += para_surface(span, n)
        for j, v in enumerate(span):
            grid2[j][i] = v
            if v != 0:
                s1 += 1

    for i, span in enumerate(grid2):
        s3 += para_surface(span, n)
    return 2*(s1 + s2 + s3)


if __name__ == '__main__':
    print(surfaceArea([[1,0],[0,2]]))
    print(surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
    print(surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))