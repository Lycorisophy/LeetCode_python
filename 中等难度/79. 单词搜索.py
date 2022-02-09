def exist(board: [[str]], word: str) -> bool:
    word = list(word)
    n = word.__len__()
    queues = [[] for _ in range(n)]
    path = []
    fisrt_letter = word[0]
    r, c = board.__len__(), board[0].__len__()
    for i in range(r):
        for j in range(c):
            letter = board[i][j]
            if letter == fisrt_letter:
                queues[0].append([i, j])
    if n == 1:
        if queues[0]:
            return True
        return False
    i = 1
    while True:
        if not queues[i-1]:
            if i == 1:
                return False
            i -= 1
            path.pop(-1)
        else:
            targer = word[i]
            cur_r, cur_c = queues[i-1].pop(0)
            targer_r, targer_c = cur_r-1, cur_c
            if 0 <= targer_r < r and 0 <= targer_c < c:
                letter = board[targer_r][targer_c]
                if letter == targer:
                    if [targer_r, targer_c] not in queues[i]:
                        if [targer_r, targer_c] not in path:
                            queues[i].append([targer_r, targer_c])
            targer_r, targer_c = cur_r + 1, cur_c
            if 0 <= targer_r < r and 0 <= targer_c < c:
                letter = board[targer_r][targer_c]
                if letter == targer:
                    if [targer_r, targer_c] not in queues[i]:
                        if [targer_r, targer_c] not in path:
                            queues[i].append([targer_r, targer_c])
            targer_r, targer_c = cur_r, cur_c + 1
            if 0 <= targer_r < r and 0 <= targer_c < c:
                letter = board[targer_r][targer_c]
                if letter == targer:
                    if [targer_r, targer_c] not in queues[i]:
                        if [targer_r, targer_c] not in path:
                            queues[i].append([targer_r, targer_c])
            targer_r, targer_c = cur_r, cur_c - 1
            if 0 <= targer_r < r and 0 <= targer_c < c:
                letter = board[targer_r][targer_c]
                if letter == targer:
                    if [targer_r, targer_c] not in queues[i]:
                        if [targer_r, targer_c] not in path:
                            queues[i].append([targer_r, targer_c])
            i += 1
            path.append([cur_r, cur_c])
            if i == n and queues[-1]:
                return True


if __name__ == '__main__':
    print(exist(board=[["A"]], word="B"))
    print(exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
    print(exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
