def search(nums: [int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = int(l + (r - l) / 2)
        o = nums[m]
        if o > target: r = m - 1
        elif o < target: l = m + 1
        else: return m
    return -1


if __name__ == '__main__':
    print(search([1],1))
    print(search([-1,0,3,5,9,12],9))
    print(search([-1,0,3,5,9,12],2))
