def removeDuplicates(nums: [int]) -> int:
    if not nums:
        return 0
    l = len(nums)
    pre = nums[0]
    i = 1
    while i < l:
        tmp = nums[i]
        if tmp == pre:
            nums.pop(i)
            l -= 1
        else:
            i += 1
            pre = tmp
    return l


if __name__ == '__main__':
    nums = []
    print(removeDuplicates(nums), nums)
