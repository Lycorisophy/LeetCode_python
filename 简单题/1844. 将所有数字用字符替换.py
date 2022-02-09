def replaceDigits(s: str) -> str:
    s = list(s)
    i = 1
    n = s.__len__()
    while i < n:
        s[i] = chr(ord(s[i-1]) + int(s[i]))
        i += 2
    return ''.join(s)


if __name__ == '__main__':
    print(replaceDigits("a1c1e1"))
    print(replaceDigits("a1b2c3d4e"))

