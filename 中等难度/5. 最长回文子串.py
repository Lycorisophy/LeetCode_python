def longestPalindrome(s: str) -> str:
    n = s.__len__()
    for i in range(n + 1, 0, -1):
        for j in range(n - i + 1):
            ss = s[j:j + i]
            if ss == ss[::-1]:
                return ss

if __name__ == '__main__':
    print(longestPalindrome("abb"))
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("a"))
    print(longestPalindrome("ac"))
