import math


def numberOfBoomerangs(points: [[int]]) -> int:
    n = points.__len__()
    if n < 3:
        return 0
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            m[i][j] = (x1-x2)**2 + (y1-y2)**2
    for j in range(n-1):
        for i in range(j+1, n):
            m[i][j] = m[j][i]
    res = 0
    for i, row in enumerate(m):
        dic = {}
        for j in range(n):
            point = row[j]
            if point not in dic:
                dic[point] = 1
            else:
                dic[point] += 1
        for v in dic.values():
            if v > 1:
                res += math.factorial(v)//math.factorial(v-2)
    return res


if __name__ == '__main__':
    print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
    print(numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))
    print(numberOfBoomerangs([[1, 1]]))
