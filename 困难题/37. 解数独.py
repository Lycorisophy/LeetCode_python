def solveSudoku(board: [[str]]) -> None:
    nums = {str(i) for i in range(1, 10)}
    rows, cols, spans = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    blanks = []
    for i, row in enumerate(board):
        for j, r in enumerate(row):
            if r != '.':
                rows[i].add(r)
                cols[j].add(r)
                a, b = i // 3, j // 3
                spans[a*3+b].add(r)
            else:
                blanks.append((i, j))

    def dfs(n):
        if n == len(blanks):
            return True
        i, j = blanks[n]
        a, b = i // 3, j // 3
        c = a * 3 + b
        cans = nums - rows[i] - cols[j] - spans[c]
        if not cans:
            return False
        for can in cans:
            board[i][j] = can
            rows[i].add(can)
            cols[j].add(can)
            spans[c].add(can)
            if dfs(n + 1):
                return True
            rows[i].remove(can)
            cols[j].remove(can)
            spans[c].remove(can)

    dfs(0)
    return board


if __name__ == '__main__':
    print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
