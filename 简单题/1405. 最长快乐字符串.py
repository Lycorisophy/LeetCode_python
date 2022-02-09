def longestDiverseString(a: int, b: int, c: int) -> str:
    arrs = [a, b, c]
    char_a = ord('a')
    res = ''
    li = -1
    while True:
        m = 0
        for i, arr in enumerate(arrs):
            if arr > m and i != li:
                m = arr
                mi = i
        li = mi
        if m >= 2:
            res += 2 * chr(li+char_a)
            arrs[li] -= 2
        elif m == 1:
            res += chr(li+char_a)
            arrs[li] = 0
        else:
            break
    return res


if __name__ == '__main__':
    print(longestDiverseString(a=1, b=1, c=7))
    print(longestDiverseString(a=2, b=2, c=1))
    print(longestDiverseString(a=7, b=1, c=0))
