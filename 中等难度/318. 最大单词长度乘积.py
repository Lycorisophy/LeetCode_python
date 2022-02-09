def maxProduct(words: [str]) -> int:
    words.sort(key=lambda x: len(x), reverse=True)
    n = len(words)
    masks = [0] * n
    lens = [0] * n
    bit_number = lambda ch: ord(ch) - ord('a')

    max_val = 0
    for i in range(n):
        bitmask = 0
        for ch in words[i]:
            bitmask |= 1 << bit_number(ch)
        masks[i] = bitmask
        lens[i] = len(words[i])
    for i in range(n):
        for j in range(i + 1, n):
            m = lens[i] * lens[j]
            if m > max_val:
                if masks[i] & masks[j] == 0:
                    max_val = m
            else:
                break
    return max_val


if __name__ == '__main__':
    print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(maxProduct(["a", "aa", "aaa", "aaaa"]))
