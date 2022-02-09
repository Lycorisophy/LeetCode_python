def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    edges = {i: [] for i in range(numCourses)}
    for prerequisite in prerequisites:
        pre, nxt = prerequisite
        edges[nxt].append(pre)

    visited = [0] * numCourses
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

    for i in range(numCourses):
        if valid and visited[i] == 0:
            dfs(i)

    if not valid:
        return False
    return True


if __name__ == '__main__':
    print(canFinish(numCourses=2, prerequisites=[[1, 0]]))
    print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
    print(canFinish(numCourses=2, prerequisites=[]))
