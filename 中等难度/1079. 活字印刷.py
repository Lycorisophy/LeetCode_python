def numTilePossibilities(tiles: str) -> int:
    n = len(tiles)
    tiles = sorted(tiles)
    visited = [False] * n
    res = 0

    def backtrack():
        nonlocal res
        for i in range(n):
            if visited[i]:
                continue
            if i > 0 and tiles[i] == tiles[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            res += 1
            backtrack()
            visited[i] = False
    backtrack()
    return res


if __name__ == '__main__':
    print(numTilePossibilities("AAB"))
    print(numTilePossibilities("AAABBC"))

