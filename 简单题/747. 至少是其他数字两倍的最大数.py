def dominantIndex(nums: [int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        index = 0
        one_num = nums[0]
        two_num = nums[1]
    else:
        index = 1
        one_num = nums[1]
        two_num = nums[0]
    if n == 2:
        if one_num >= two_num * 2:
            return index
        return -1
    for i in range(2, n):
        t = nums[i]
        if t > one_num:
            index = i
            two_num = one_num
            one_num = t
        elif t > two_num:
            two_num = t
    if one_num >= two_num * 2:
        return index
    return -1


if __name__ == '__main__':
    print(dominantIndex([3, 6, 8, 0]))
    print(dominantIndex([1, 2, 6, 4]))
    print(dominantIndex([3, 6, 1, 0, 15]))
