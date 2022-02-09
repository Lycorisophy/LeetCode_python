import heapq


def trapRainWater(heightMap: [[int]]) -> int:
    m, n = len(heightMap), len(heightMap[0])
    if m <= 2 or n <= 2:
        return 0
    visited = set()
    heap = []
    for i in range(m):
        heapq.heappush(heap, (heightMap[i][0], i, 0))
        heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
        visited.add((i, 0))
        visited.add((i, n - 1))
    for j in range(1, n - 1):
        heapq.heappush(heap, (heightMap[0][j], 0, j))
        heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
        visited.add((0, j))
        visited.add((m - 1, j))

    ans = 0
    while heap:
        h, i, j = heapq.heappop(heap)
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + x, j + y
            if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                near_h = heightMap[new_i][new_j]
                if near_h < h:
                    ans += h - near_h
                heapq.heappush(heap, (max(h, near_h), new_i, new_j))
                visited.add((new_i, new_j))
    return ans


if __name__ == '__main__':
    print(trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
    print(trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
