def removePalindromeSub(s: str) -> int:
    return (1 if s == s[::-1] else 2) if s else 0


if __name__ == '__main__':
    print(removePalindromeSub("bbaabaaa"))

