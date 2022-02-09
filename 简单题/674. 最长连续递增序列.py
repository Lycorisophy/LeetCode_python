def findLengthOfLCIS(nums: [int]) -> int:
    l = len(nums)
    if l == 0 or l == 1:
        return l
    tmp, max = 1, 1
    pre = nums[0]
    for i in range(1, l):
        if nums[i] > pre:
            tmp += 1
        else:
            if tmp > max:
                max = tmp
            tmp = 1
        pre = nums[i]
    return max if max > tmp else tmp


if __name__ == '__main__':
    print(findLengthOfLCIS([1,3,1,4,7]))
    print(findLengthOfLCIS([2,2,3,2,2]))
    print(findLengthOfLCIS([1,1]))
