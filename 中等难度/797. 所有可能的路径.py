def allPathsSourceTarget(graph: [[int]]) -> [[int]]:
    n = graph.__len__()

    def dfs(node, target):
        if node == target:
            return [[target]]
        ans = []
        for nei in graph[node]:
            for path in dfs(nei, target):
                ans.append([node] + path)
        return ans

    return dfs(0, n-1)


if __name__ == '__main__':
    print(allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
    print(allPathsSourceTarget([[1],[]]))
