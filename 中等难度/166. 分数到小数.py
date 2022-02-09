def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return '0'
    is_fushu = False
    if numerator < 0:
        numerator = 0 - numerator
        is_fushu = True
    if denominator < 0:
        denominator = 0 - denominator
        if is_fushu:
            is_fushu = False
        else:
            is_fushu = True
    res = []
    numerators = {}
    i = 0
    numerators[numerator] = i
    while numerator < denominator:
        res.append(0)
        i += 1
        numerator *= 10
        numerators[numerator] = i
    a, b = divmod(numerator, denominator)
    res.append(a)
    start = -1
    while b != 0:
        b *= 10
        i += 1
        if b in numerators:
            start = numerators[b]
            break
        numerators[b] = i
        while b < denominator:
            res.append(0)
            i += 1
            b *= 10
            if b in numerators:
                start = numerators[b]
                break
            numerators[b] = i
        a, b = divmod(b, denominator)
        res.append(a)
    n = res.__len__()
    first = res[0]
    if is_fushu:
        ans = '-'+str(first)
    else:
        ans = str(first)
    if n == 1:
        return ans
    ans += '.'
    if start == -1:
        for i in range(1, n):
            ans += str(res[i])
    else:
        for i in range(1, start):
            ans += str(res[i])
        ans += '('
        for i in range(start, n):
            ans += str(res[i])
        ans += ')'
    return ans


if __name__ == '__main__':
    print(fractionToDecimal(5, 4))
    print(fractionToDecimal(4, 333))
    print(fractionToDecimal(1, 2))
    print(fractionToDecimal(2, 1))
    print(fractionToDecimal(2, 3))
    print(fractionToDecimal(1, 5))
    print(fractionToDecimal(3, 2))
