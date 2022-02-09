def lengthOfLongestSubstring(s: str) -> int:
    indexs = {}
    res = 0
    max_res = 0
    n = s.__len__()
    i = 0
    while i < n:
        char = s[i]
        if char in indexs:
            if res > max_res:
                max_res = res
            i = indexs[char] + 1
            res = 0
            indexs = {}
        else:
            res += 1
            indexs[char] = i
            i += 1
    return res if res > max_res else max_res


if __name__ == '__main__':
    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring(""))
