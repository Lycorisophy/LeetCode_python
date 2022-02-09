def validPalindrome(s: str) -> bool:
    l = len(s)
    i, j, k = 0, l - 1, 0
    while i < j:
        if s[i] != s[j]:
            k += 1
            if k == 2:
                i, j, k = 0, l - 1, 0
                while i < j:
                    if s[i] != s[j]:
                        k += 1
                        if k == 2:
                            return False
                    else:
                        j -= 1
                    i += 1
                return True
        else:
            i += 1
        j -= 1
    return True


if __name__ == '__main__':
    print(validPalindrome("abcd"))
