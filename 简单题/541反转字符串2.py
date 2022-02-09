def reverseStr(s: str, k: int) -> str:
    c, d = 0, 0
    res = ''
    tmp = ''
    for letter in s:
        tmp += letter
        c += 1
        if c == k:
            c = 0
            if d == 1:
                d = 0
                res += tmp
                tmp = ''
            elif d == 0:
                d = 1
                res += tmp[::-1]
                tmp = ''
    if letter != '':
        if d == 1:
            res += tmp
        elif d == 0:
            res += tmp[::-1]
    return res


if __name__ == '__main__':
    print(reverseStr(s = "ab", k = 3))
    print(reverseStr(s = "abcdefgfjslkajdsa", k = 5))