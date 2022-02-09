def countBinarySubstrings(s: str) -> int:
    l = len(s)
    if l < 2:
        return 0
    cnt, res, pre_c = 1, 0, 0
    pre = s[0]
    for i in range(1, l):
        if s[i] == pre:
            cnt += 1
        else:
            pre = s[i]
            pre_c = cnt
            cnt = 1
            break
    for j in range(i+1, l):
        if s[j] == pre:
            cnt += 1
        else:
            pre = s[j]
            res += min(pre_c, cnt)
            pre_c = cnt
            cnt = 1
    res += min(cnt, pre_c)
    return res


if __name__ == '__main__':
    print(countBinarySubstrings("00"))
    print(countBinarySubstrings("10101"))
    print(countBinarySubstrings("101010011"))
