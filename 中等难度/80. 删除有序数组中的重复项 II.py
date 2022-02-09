def removeDuplicates(nums: [int]) -> int:
    n = nums.__len__()
    if n < 3:
        return n
    pre = nums[0]
    i = 1
    cnt = 1
    while i < n:
        num = nums[i]
        if num != pre:
            pre = num
            cnt = 1
            i += 1
        else:
            cnt += 1
            if cnt == 3:
                cnt = 2
                nums.pop(i)
                n -= 1
            else:
                i += 1
    return n


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(removeDuplicates([1]))
    print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 66]))
    print(removeDuplicates([1, 2]))
