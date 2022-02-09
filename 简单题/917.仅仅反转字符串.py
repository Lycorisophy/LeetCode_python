def reverseOnlyLetters(S: str) -> str:
    S = list(S)
    i, j = 0, S.__len__()-1
    while i < j:
        if not S[i].isalpha():
            i += 1
        elif not S[j].isalpha():
                j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
    return ''.join(S)


if __name__ == '__main__':
    print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))

