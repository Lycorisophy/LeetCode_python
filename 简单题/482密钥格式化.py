def licenseKeyFormatting(S: str, K: int) -> str:
    res = ''
    c = 0
    for s in S[::-1]:
        if s != '-':
            if c == K:
                c = 0
                res += '-'
            if s.islower():
                res += s.capitalize()
            elif s.isupper():
                res += s
            else:
                res += s
            c += 1
    return res[::-1]


if __name__ == '__main__':
    print(licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4))
    print(licenseKeyFormatting(S = "2-5g-3-J", K = 2))