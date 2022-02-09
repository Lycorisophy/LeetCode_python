def canMakeArithmeticProgression(arr: [int]) -> bool:
    n = arr.__len__()
    if n < 3:
        return True
    arr.sort()
    a1, a2 = arr[0], arr[1]
    gap = a2 - a1
    pre = a2
    for i in range(2, n):
        tmp = arr[i]
        if tmp - pre != gap:
            return False
        pre = tmp
    return True


if __name__ == '__main__':
    print(canMakeArithmeticProgression([3, 5, 1]))
    print(canMakeArithmeticProgression([1, 2, 4]))
