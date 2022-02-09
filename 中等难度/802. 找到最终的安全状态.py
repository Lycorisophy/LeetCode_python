def eventualSafeNodes(graph: [[int]]) -> [int]:
    n = len(graph)
    color = [0] * n

    def dfs(node) -> bool:
        if color[node] > 0:
            return color[node] == 2
        color[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        color[node] = 2
        return True

    return [i for i in range(n) if dfs(i)]


if __name__ == '__main__':
    print(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
