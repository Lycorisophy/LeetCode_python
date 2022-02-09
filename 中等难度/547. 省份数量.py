def findCircleNum(isConnected: [[int]]) -> int:
    def dfs(x: int):
        for y in range(n):
            if isConnected[x][y] == 1 and y not in visited:
                visited.add(y)
                dfs(y)

    n = isConnected.__len__()
    visited = set()
    circles = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            circles += 1
    return circles


if __name__ == '__main__':
    print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))

