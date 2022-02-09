def fraction(cont: [int]) -> [int]:
    n = cont.__len__()
    if n == 1:
        return [cont[0], 1]
    a, b = cont[-1], 1
    for i in range(n - 2, 0, -1):
        a, b = b, a
        num = cont[i]
        a += num * b
    return [b+cont[0]*a, a]


if __name__ == '__main__':
    print(fraction([3, 2, 0, 2]))
    print(fraction([0, 0, 3]))
