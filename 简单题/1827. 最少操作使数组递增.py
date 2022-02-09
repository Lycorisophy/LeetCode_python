def minOperations(nums: [int]) -> int:
    n = nums.__len__()
    if n == 1:
        return 0
    pre = nums[0]
    res = 0
    for num in nums[1:]:
        if num <= pre:
            res += pre-num+1
            pre += 1
        else:
            pre = num
    return res


if __name__ == '__main__':
    print(minOperations([1,1,1]))
    print(minOperations([1,5,2,4,1]))
    print(minOperations([8]))
