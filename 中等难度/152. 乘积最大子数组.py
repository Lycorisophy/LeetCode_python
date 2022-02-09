def maxProduct(nums: [int]) -> int:
    t = nums.__len__()
    if t == 1:
        return nums[0]
    maxF = nums[0]
    minF = maxF
    ans = maxF
    for a in nums[1:]:
        mx = maxF
        mn = minF
        maxF = max(mx * a, max(a, mn * a))
        minF = min(mn * a, min(a, mx * a))
        ans = max(maxF, ans)
    return ans


if __name__ == '__main__':
    print(maxProduct([0]))
    print(maxProduct([0, 0]))
    print(maxProduct([1]))
    print(maxProduct([0, 1, 0]))
    print(maxProduct([0, -1, 0]))
    print(maxProduct([2, 3, -2, 4]))
    print(maxProduct([-2, 0, -1]))
