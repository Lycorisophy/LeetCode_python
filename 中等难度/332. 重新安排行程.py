import collections
import heapq


def findItinerary(tickets: [[str]]) -> [str]:
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

    dfs("JFK")
    return stack[::-1]



if __name__ == '__main__':
    print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
    print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
