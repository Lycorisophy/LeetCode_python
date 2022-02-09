def numDecodings(s: str) -> int:
    mod = 10 ** 9 + 7

    def check1digit(ch: str) -> int:
        if ch == "0":
            return 0
        return 9 if ch == "*" else 1

    def check2digits(c0: str, c1: str) -> int:
        if c0 == c1 == "*":
            return 15
        if c0 == "*":
            return 2 if c1 <= "6" else 1
        if c1 == "*":
            return 9 if c0 == "1" else (6 if c0 == "2" else 0)
        return int(c0 != "0" and int(c0) * 10 + int(c1) <= 26)

    n = len(s)
    a, b, c = 0, 1, 0
    for i in range(1, n + 1):
        c = b * check1digit(s[i - 1])
        if i > 1:
            c += a * check2digits(s[i - 2], s[i - 1])
        c %= mod
        a = b
        b = c
    return c


if __name__ == '__main__':
    print(numDecodings("*"))
    print(numDecodings("1*"))
    print(numDecodings("2*"))
