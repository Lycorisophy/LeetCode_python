def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(x, y):
        if x % y == 0:
            return y
        return gcd(y, x % y)

    n1, n2 = str1.__len__(), str2.__len__()
    gn = gcd(n1, n2)
    n = gn
    while n > 0:
        if gn % n == 0:
            tmp = str1[:n]
            if tmp == str2[:n]:
                if str1[n:] + tmp == str1:
                    if str2[n:] + tmp == str2:
                        return tmp
        n -= 1
    return ''


if __name__ == '__main__':
    print(gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
    print(gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
    print(gcdOfStrings(str1 = "LEET", str2 = "CODE"))
