from collections import Counter


def countKDifference(nums: [int], k: int) -> int:
    res = 0
    cnt = Counter()
    for num in nums:
        res += cnt[num - k] + cnt[num + k]
        cnt[num] += 1
    return res


if __name__ == '__main__':
    print(countKDifference(nums = [1,2,2,1], k = 1))
    print(countKDifference(nums = [1,3], k = 3))
    print(countKDifference(nums = [3,2,1,5,4], k = 2))
