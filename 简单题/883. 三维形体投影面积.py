def projectionArea(grid: [[int]]) -> int:
    s1, s2, s3 = 0, 0, []
    for i, span in enumerate(grid):
        s2 += max(span)
        for j, v in enumerate(span):
            try:
                s3[j] = max(s3[j], v)
            except IndexError:
                s3.append(v)
            if v != 0:
                s1 += 1
    return s1 + s2 + sum(s3)


if __name__ == '__main__':
    print(projectionArea([[1, 2], [3, 4]]))
    print(projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
