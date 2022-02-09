def tictactoe(moves: [[int]]) -> str:
    n = moves.__len__()
    if n < 5:
        return 'Pending'
    win_sets = [
        set([(0, 0), (0, 1), (0, 2)]),
        set([(1, 0), (1, 1), (1, 2)]),
        set([(2, 0), (2, 1), (2, 2)]),
        set([(0, 0), (1, 0), (2, 0)]),
        set([(0, 1), (1, 1), (2, 1)]),
        set([(0, 2), (1, 2), (2, 2)]),
        set([(0, 0), (1, 1), (2, 2)]),
        set([(0, 2), (1, 1), (2, 0)])]
    last = tuple(moves[-1])
    a_moves, b_moves = set(), set()
    for i, move in enumerate(moves):
        if i % 2 == 0:
            a_moves.add(tuple(move))
        else:
            b_moves.add(tuple(move))
    if n % 2 == 1:
        for win_set in win_sets:
            if last in win_set:
                if len(win_set & a_moves) == 3:
                    return 'A'
    else:
        for win_set in win_sets:
            if last in win_set:
                if len(win_set & b_moves) == 3:
                    return 'B'
    if n < 9:
        return 'Pending'
    return 'Draw'


if __name__ == '__main__':
    print(tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
    print(tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
    print(tictactoe(moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
    print(tictactoe([[0, 0], [1, 1]]))
