def findIntegers(num: int) -> int:
    cnt = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
           46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
    pre = 0
    res = 0

    for i in range(29, -1, -1):
        val = (1 << i)
        if num & val:
            num -= val
            res += cnt[i + 1]
            if pre == 1:
                break
            pre = 1
        else:
            pre = 0
        if i == 0:
            res += 1
    return res


if __name__ == '__main__':
    x = 5
    y = findIntegers(x)
    print(y)
