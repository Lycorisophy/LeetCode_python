def findRedundantConnection(edges: [[int]]) -> [int]:
    n = edges.__len__()
    S = list(range(n + 1))

    def find(X):
        return S[X] if S[X] == X else find(S[X])

    def union(X, Y):
        S[find(X)] = find(Y)

    for node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
        else:
            return [node1, node2]
    return


if __name__ == '__main__':
    print(findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    print(findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
