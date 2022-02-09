def isAdditiveNumber(num: str) -> bool:
    n = num.__len__()
    if n < 3:
        return False

    def backtrack(n1: [], n2: [], r: []) -> bool:
        s = str(int(n1) + int(n2))
        if s == r:
            return True
        elif len(s) > len(r) or r[:len(s)] != s:
            return False
        return backtrack(n2, s, r[len(s):])

    for i in range(1, n + 1):
        for j in range(i + 1, n):
            num1, num2, rest = num[:i], num[i:j], num[j:]
            if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                continue
            if backtrack(num1, num2, rest):
                return True
    return False


if __name__ == '__main__':
    print(isAdditiveNumber("112358"))
    print(isAdditiveNumber("1123115"))
    print(isAdditiveNumber("199100199"))
    print(isAdditiveNumber("19910019"))
