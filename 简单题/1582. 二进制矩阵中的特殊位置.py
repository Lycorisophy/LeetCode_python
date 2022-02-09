def numSpecial(mat: [[int]]) -> int:
    res = 0
    rs = [sum(r) for r in mat]
    cs = [sum(c) for c in zip(*mat)]
    for i, r in enumerate(mat):
        for j, m in enumerate(r):
            if m == 1:
                if rs[i] == 1 and cs[j] == 1:
                    res += 1
    return res


if __name__ == '__main__':
    print(numSpecial([[0,0,1,0],[0,0,0,1],[1,0,1,0],[0,0,0,0]]))
    print(numSpecial([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]))
    print(numSpecial([[0, 0, 0, 1],
                      [1, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]
                     ))
    print(numSpecial([[0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1]]
                     ))
