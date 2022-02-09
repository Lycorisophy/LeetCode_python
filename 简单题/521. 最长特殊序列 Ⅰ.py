def findLUSlength(a: str, b: str) -> int:
    return max(len(a), len(b)) if a != b else -1


if __name__ == '__main__':
    print(findLUSlength("aba", "cdc"))
    print(findLUSlength(a = "aaa", b = "bbb"))
    print(findLUSlength(a = "aaa", b = "aaa"))