def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    if haystack == '':
        return -1
    l1, l2 = len(haystack), len(needle)
    i = 0
    while i <= l1-l2:
        j = i
        for k, n in enumerate(needle):
            if haystack[j] != n:
                break
            if k == l2-1:
                return i
            j += 1
        i += 1
    return -1


if __name__ == '__main__':
    print(strStr(haystack = "hello", needle = "ll"))
    print(strStr(haystack = "aaaaa", needle = "bba"))
    print(strStr(haystack = "aaaaa", needle = ""))
    print(strStr(haystack = "", needle = "bba"))