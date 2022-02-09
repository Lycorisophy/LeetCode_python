def largestTriangleArea(points: [[int]]) -> float:
    res = 0
    for A in points:
        for B in points:
            for C in points:
                res = max(res,
                          A[0] * B[1] + B[0] * C[1] + C[0] * A[1] -
                          A[0] * C[1] - C[0] * B[1] - B[0] * A[1])
    return res / 2


if __name__ == '__main__':
    print(largestTriangleArea([[4,6],[6,5],[3,1]]))
