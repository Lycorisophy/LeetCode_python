import math


def nearestValidPoint(x: int, y: int, points: [[int]]) -> int:
    min_dis = 10000
    res = -1
    for i, point in enumerate(points):
        a, b = point
        if a == x:
            dis = abs(b-y)
            if dis < min_dis:
                res = i
                min_dis = dis
        elif b == y:
            dis = abs(a-x)
            if dis < min_dis:
                res = i
                min_dis = dis
    return res


if __name__ == '__main__':
    print(nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
    print(nearestValidPoint(x=3, y=4, points=[[3, 4]]))
    print(nearestValidPoint(x=3, y=4, points=[[2, 3]]))
