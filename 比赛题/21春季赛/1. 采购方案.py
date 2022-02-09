from collections import Counter
from functools import reduce


def purchasePlans(nums: [int], target: int) -> int:
    res = 0
    nums.sort()
    while True:
        if nums:
            if nums[-1] >= target:
                nums.pop(-1)
            else:
                break
        else:
            return 0
    n = nums.__len__()
    max_n = n - 1
    for i in range(n - 1):
        do_plus = False
        tmp = nums[i]
        for j in range(max_n, i, -1):
            if tmp + nums[j] <= target:
                max_n = j
                do_plus = True
                break
        if do_plus:
            res += j - i
    return int(res % (1e9 + 7))


if __name__ == '__main__':
    print(purchasePlans(nums=[2, 5], target=1))
    print(purchasePlans(nums=[2, 2, 1, 9], target=10))
    print(purchasePlans(nums=[2, 2, 8, 10, 11, 1, 1, 2, 2, 4, 4, 6, 6, 7, 8, 9, 9, 9, 1, 1, 2], target=10000))
