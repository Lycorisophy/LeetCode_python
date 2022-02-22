def findCenter(edges: [[int]]) -> int:
    u, v = edges[0]
    nu, nv = edges[1]
    if u == nu or u == nv:
        return u
    return v


if __name__ == '__main__':
    print(findCenter([[1, 2], [2, 3], [4, 2]]))
    print(findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))
