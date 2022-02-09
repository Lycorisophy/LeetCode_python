def canVisitAllRooms(rooms: [[int]]) -> bool:
    n = len(rooms)
    q = [0]
    visited = [False] * n
    while q:
        t = q.pop()
        visited[t] = True
        for room in rooms[t]:
            if not visited[room]:
                q.append(room)
    return True if all(visited) else False


if __name__ == '__main__':
    print(canVisitAllRooms([[1], [2], [3], []]))
    print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
