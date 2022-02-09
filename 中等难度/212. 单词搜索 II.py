def findWords(board: [[str]], words: [str]) -> [str]:
    res = []
    for word in words:
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
        i = 1
        while True:
            if n == 1:
                if queues[0]:
                    res.append(word)
                break
            if i == n:
                i = 1
            if not queues[i - 1]:
                if i == 1:
                    break
                i -= 1
                path.pop(-1)
            else:
                targer = word[i]
                cur_r, cur_c = queues[i - 1].pop(0)
                targer_r, targer_c = cur_r - 1, cur_c
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
                    res.append(word)
                    break
    return res


if __name__ == '__main__':
    print(findWords([["a","b"]],
                    ["a","b"]))
    print(findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
    print(findWords(board=[["A"]], words=["A"]))
