def subSort(array: [int]) -> [int]:
    n = len(array)
    maxx, minn = -float("inf"), float("inf")
    l, r = -1, -1
    for i in range(n):
        if array[i] < maxx:  # 找到右边居然有值大于max，那么这是右边界
            r = i
        else:
            maxx = array[i]

        if array[n - 1 - i] > minn:
            l = n - 1 - i
        else:
            minn = array[n - 1 - i]

    return [l, r]


if __name__ == '__main__':
    print(subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
    print(subSort([1, 2, 4, 7, 10, 11]))
    print(subSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
