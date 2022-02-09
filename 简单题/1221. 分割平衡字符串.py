def balancedStringSplit(s: str) -> int:
    r, l, res = 0, 0, 0
    for S in s:
        if S == 'R':
            r += 1
        else:
            l += 1
        if r == l:
            r, l = 0, 0
            res += 1
    return res


if __name__ == '__main__':
    print(balancedStringSplit(s="RLRRLLRLRL"))
    print(balancedStringSplit(s="RLLLLRRRLR"))
    print(balancedStringSplit(s="LLLLRRRR"))
    print(balancedStringSplit(s="RLRRRLLRLL"))
