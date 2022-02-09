def findMin(nums: [int]) -> int:
    n = nums.__len__()
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        L, M, R = nums[l], nums[m], nums[r]
        if m == l:
            return min(L, R)
        if L < R:
            return L
        else:
            if M < R:
                if nums[m-1] > M:
                    return M
                r = m - 1
            else:
                l = m + 1



if __name__ == '__main__':
    print(findMin([3, 4, 5, 1, 2]))
    print(findMin([4, 5, 6, 7, 0, 1, 2]))
    print(findMin([11, 13, 15, 17]))
    print(findMin([0]))
    print(findMin([0, 1]))
    print(findMin([1, 0]))
    print(findMin([0, 1, 2]))
    print(findMin([2, 0, 1]))
    print(findMin([1, 2, 0]))
