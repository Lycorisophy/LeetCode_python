def checkPossibility(nums: [int]) -> bool:
    i, j, k = 0, 0, 0
    pre = nums[0]
    while j < len(nums)-1:
        j += 1
        if nums[i] > nums[j]:
            if pre > nums[j] and i != 0 and pre > nums[i]:
                return False
            k += 1
            if k == 2:
                return False
            if i != 0:
                if pre <= nums[j]:
                    nums[i] = nums[j]
                    pre = nums[i]
                else:
                    nums[j] = nums[i]
        else:
           pre = nums[i]
        i += 1
    return True


if __name__ == '__main__':
    print(checkPossibility([-1,4,2,3]))

