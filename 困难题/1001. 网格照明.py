def gridIllumination(n: int, lamps: [[int]], queries: [[int]]) -> [int]:
    arrs = [[0 for _ in range(n)] for _ in range(n)]
    max_light = 4 * n

    def open(x: int, y: int):
        arrs[x][y] += max_light
        for i in range(n):
            if i != x:
                arrs[i][y] += 1
                dy1 = i - x + y
                dy2 = x - i + y
                if 0 <= dy1 < n:
                    arrs[i][dy1] += 1
                if 0 <= dy2 < n:
                    arrs[i][dy2] += 1
            if i != y:
                arrs[x][i] += 1

    def close(x: int, y: int):
        arrs[x][y] -= max_light
        for i in range(n):
            if i != x:
                arrs[i][y] -= 1
                dy1 = i - x + y
                dy2 = x - i + y
                if 0 <= dy1 < n:
                    arrs[i][dy1] -= 1
                if 0 <= dy2 < n:
                    arrs[i][dy2] -= 1
            if i != y:
                arrs[x][i] -= 1

    for lamp in lamps:
        a, b = lamp
        if arrs[a][b] < max_light:
            open(a, b)
    for arr in arrs:
        print(arr)
    print()
    res = [0] * len(queries)
    for i, query in enumerate(queries):
        a, b = query
        if arrs[a][b] > 0:
            res[i] = 1
        for dx, dy in (0, 1), (1, 0), (0, -1), (0, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1):
            da, db = a + dx, b + dy
            if 0 <= da < n and 0 <= db < n and arrs[da][db] >= max_light:
                close(da, db)
        for arr in arrs:
            print(arr)
        print()
    return res


if __name__ == '__main__':
    print(gridIllumination(5,
                           [[0, 0], [0, 4]],
                           [[0, 4], [0, 1], [1, 4]]))
