def pivotIndex(nums: [int]) -> int:
    l = len(nums)
    if l == 0 or l == 1:
        return 0
    pre = nums[0]
    s1, s2 = 0, sum(nums)-pre
    if s1 == s2:
        return 0
    for i in range(1, l):
        t = nums[i]
        s1 += pre
        s2 -= t
        pre = t
        if s1 == s2:
            return i
    return -1


if __name__ == '__main__':
    print(pivotIndex([-1,-1,0,1,1,0]))
    print(pivotIndex([1, 2, 3]))
    print(pivotIndex([2, 1, -1]))
