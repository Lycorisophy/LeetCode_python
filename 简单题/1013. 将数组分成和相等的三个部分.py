def canThreePartsEqualSum(arr: [int]) -> bool:
    n = arr.__len__()
    S = sum(arr)
    if S % 3 != 0:
        return False
    s = S // 3
    tmp = 0
    cnt = 0
    for i, a in enumerate(arr):
        tmp += a
        if tmp == s:
            cnt += 1
            if cnt == 2 and i != n:
                return True
            tmp = 0
    return False


if __name__ == '__main__':
    print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    print(canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
    print(canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
