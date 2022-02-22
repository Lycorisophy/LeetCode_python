def numberOfGoodSubsets(nums: [int]) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    mod = 10 ** 9 + 7
    cnt = [0] * 31
    for num in nums:
        cnt[num] += 1
    return


if __name__ == '__main__':
    print(numberOfGoodSubsets([1, 2, 3, 4]))
    print(numberOfGoodSubsets([4, 2, 3, 15]))
