import collections
import heapq


# 有向图的遍历
def findItinerary(tickets: [[str]], root: str) -> [str]:
    vec = collections.defaultdict(list)
    for depart, arrive in tickets:
        vec[depart].append(arrive)
    for key in vec:
        heapq.heapify(vec[key])
    stack = list()

    def dfs(curr: str):
        while vec[curr]:
            tmp = heapq.heappop(vec[curr])
            dfs(tmp)
        stack.append(curr)

    dfs(root)
    return stack[::-1]


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
    print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
    print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))