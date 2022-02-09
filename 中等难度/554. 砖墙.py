def leastBricks(wall: [[int]]) -> int:
    widthCount = dict()
    n = wall.__len__()
    for row in wall:
        length = 0
        for i in range(0, row.__len__()-1):
            length += row[i]
            if length in widthCount:
                widthCount[length] += 1
            else:
                widthCount[length] = 1
    res = 0
    for count in widthCount.values():
        res = max(count, res)
    return n - res


if __name__ == '__main__':
    print(leastBricks([[1, 1], [2], [1, 1]]))
    print(leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
    print(leastBricks([[1], [1], [1]]))
