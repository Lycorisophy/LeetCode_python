def numWays(n: int, relation: [[int]], k: int) -> int:
    ways = [[] for _ in range(n)]
    for rel in relation:
        a, b = rel
        ways[a].append(b)

    def getWays(rels, res, j):
        if rels:
            if j != k:
                for rel in rels:
                    res = getWays(ways[rel], res, j+1)
            else:
                for rel in rels:
                    if rel == n-1:
                        res += 1
                return res
        return res

    return getWays(ways[0], 0, 1)


if __name__ == '__main__':
    print(numWays(n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3

))
    print(numWays(n = 3, relation = [[0,2],[2,1]], k = 2))

