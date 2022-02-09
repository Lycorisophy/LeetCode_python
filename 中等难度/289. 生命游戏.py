def gameOfLife(board: [[int]]) -> None:
    n = board.__len__()
    m = board[0].__len__()
    def alive(x, y):
        nonlocal n, m
        cnt = 0
        for e in range(x-1, x+2):
            for f in range(y-1, y+2):
                if 0 <= e < n and 0 <= f < m:
                    z = board[e][f]
                    if z == 1 or z == 3:
                        cnt += 1
        return cnt == 3

    def godie(x, y):
        nonlocal n, m
        cnt = 0
        for e in range(x-1, x+2):
            for f in range(y-1, y+2):
                if 0 <= e < n and 0 <= f < m:
                    z = board[e][f]
                    if z == 1 or z == 3:
                        cnt += 1
        return cnt > 4 or cnt < 3

    for i, row in enumerate(board):
        for j, b in enumerate(row):
            if b == 0:
                if alive(i, j):
                    board[i][j] = 2
            else:
                if godie(i, j):
                    board[i][j] = 3
    for i, row in enumerate(board):
        for j, b in enumerate(row):
            if b == 2:
                board[i][j] = 1
            if b == 3:
                board[i][j] = 0

    return board

if __name__ == '__main__':
    print(gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    print(gameOfLife([[1, 1], [1, 0]]))
