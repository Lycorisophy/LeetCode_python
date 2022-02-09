def firstUniqChar(s: str) -> int:
    m = {}
    for i, data in enumerate(s):
        try:
            m[data] += 1
        except KeyError:
            m[data] = 1
    for i, data in enumerate(s):
        if m[data] == 1:
            return i
    return -1


if __name__ == '__main__':
    print(firstUniqChar(s = "loveleetcode"))