def findOrder(numCourses: int, prerequisites: [[int]]) -> [int]:
    edges = {i: [] for i in range(numCourses)}
    for prerequisite in prerequisites:
        pre, nxt = prerequisite
        edges[nxt].append(pre)

    visited = [0] * numCourses
    res = []
    valid = True

    def dfs(u: int):
        nonlocal valid
        visited[u] = 1
        for v in edges[u]:
            if visited[v] == 0:
                dfs(v)
                if not valid:
                    return
            elif visited[v] == 1:
                valid = False
                return
        visited[u] = 2
        res.append(u)

    for i in range(numCourses):
        if valid and visited[i] == 0:
            dfs(i)

    if not valid:
        return []
    return res[::-1]


if __name__ == '__main__':
    print(findOrder(2, [[1, 0]]))
    print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
