def maxPower(s: str) -> int:
    n = s.__len__()
    res, tmp = 1, 1
    l, r = 0, 1
    while r < n:
        if s[l] == s[r]:
            r += 1
            tmp += 1
        else:
            res = max(tmp, res)
            tmp = 1
            l, r = r, r+1
    return max(tmp, res)


if __name__ == '__main__':
    print(maxPower("leetcode"))
    print(maxPower("abbcccddddeeeeedcba"))
    print(maxPower("triplepillooooow"))
    print(maxPower("hooraaaaaaaaaaay"))
    print(maxPower("tourist"))
