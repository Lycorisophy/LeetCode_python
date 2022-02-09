def binaryGap(n: int) -> int:
    bn = bin(n)[2:]
    res = 0
    for i, b in enumerate(bn):
        if b == '1':
            start = i
            break
    for j in range(i, len(bn)):
        if bn[j] == '1':
            res = max(j-start, res)
            start = j
    return res


if __name__ == '__main__':
    print(binaryGap(1025))
    print(binaryGap(111))
    print(binaryGap(5))
