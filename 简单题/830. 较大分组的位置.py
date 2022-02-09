def largeGroupPositions(s: str) -> [[int]]:
    res = []
    start = 0
    pre = s[0]
    for i, letter in enumerate(s):
        if letter != pre:
            if i - start >= 3:
                res.append([start, i - 1])
            pre = letter
            start = i
    if letter == pre:
        if i - start >= 2:
            res.append([start, i])
    return res


if __name__ == '__main__':
    print(largeGroupPositions("aaa"))

