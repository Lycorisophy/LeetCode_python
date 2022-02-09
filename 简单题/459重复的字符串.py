def repeatedSubstringPattern(s: str) -> bool:
    for i in range(1, len(s)//2+1):
        if s == s[i:]+s[:i]:
            return True
    return False


if __name__ == '__main__':
    print(repeatedSubstringPattern("abab"))
    print(repeatedSubstringPattern("aba"))
    print(repeatedSubstringPattern("abcabcabcabc"))
    print(repeatedSubstringPattern("abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"))
