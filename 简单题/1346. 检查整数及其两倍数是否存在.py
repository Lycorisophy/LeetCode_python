def checkIfExist(arr: [int]) -> bool:
    s = set()
    for a in arr:
        half = a // 2
        j = half << 1
        if (j == a and half in s) or a << 1 in s:
            return True
        s.add(a)
    return False


if __name__ == '__main__':
    print(checkIfExist([0]))
    print(checkIfExist([0, 0]))
    print(checkIfExist([-3, -6, 14, 11]))

