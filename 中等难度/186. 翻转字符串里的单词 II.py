def reverseWords(s: [str]) -> None:
    n = len(s)
    l = -1
    for i, S in enumerate(s):
        if S == ' ':
            j, k = l + 1, i - 1
            while j < k:
                s[j], s[k] = s[k], s[j]
                j += 1
                k -= 1
            l = i
    j, k = l + 1, i
    while j < k:
        s[j], s[k] = s[k], s[j]
        j += 1
        k -= 1
    j, k = 0, n-1
    while j < k:
        s[j], s[k] = s[k], s[j]
        j += 1
        k -= 1
    return s


if __name__ == '__main__':
    print(reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
