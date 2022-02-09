def totalHammingDistance(nums: [int]) -> int:
    n = nums.__len__()
    if n < 2:
        return 0
    cnt = [0 for _ in range(30)]
    for num in nums:
        num = bin(num)[2:]
        m = num.__len__()
        for i, char in enumerate(num):
            if char == '1':
                cnt[-m+i] += 1
    res = 0
    for c in cnt:
        res += c * (n-c)
    return res


if __name__ == '__main__':
    print(totalHammingDistance([4,14,2]))
    print(totalHammingDistance([4,14,4]))
